import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings # Local embeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# Streamlit app title
st.title("AI-Powered PDF Q&A")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

def load_document(file):
    """Extract text from the PDF."""
    pdf_reader = PdfReader(file)
    text = "".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
    return text

def create_vector_store(text):
    """Create a FAISS vector store with local embeddings."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(text)

    # Use Hugging Face embeddings instead of OpenAI
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    docsearch = FAISS.from_texts(texts, embeddings)

    return docsearch

if uploaded_file:
    # Load and process document
    document_text = load_document(uploaded_file)
    vector_store = create_vector_store(document_text)
    st.write("Document processed successfully!")

    llm = Ollama(model="mistral")
    
    # Set up retrieval-based QA
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vector_store.as_retriever(), chain_type="stuff")

    # Query input
    query = st.text_input("Ask a question about the document:")

    if query:
        answer = qa_chain.run(query)
        st.write("Answer:", answer)
