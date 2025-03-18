import streamlit as st
import speech_recognition as sr
import pyttsx3
import threading
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains.question_answering import load_qa_chain

# Initialize TTS engine globally
tts_engine = pyttsx3.init()

# Streamlit App Title
st.title("AI-Powered PDF Assistant with Voice & Text")

# Initialize session state for answer storage and TTS control
if "answer" not in st.session_state:
    st.session_state.answer = ""

if "is_speaking" not in st.session_state:
    st.session_state.is_speaking = False  # Track whether speech is playing

# Option to choose input mode
mode = st.radio("Choose Input Mode:", ["Text", "Voice"])

# File uploader for PDFs
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Function to extract text from PDF
def load_document(file):
    pdf_reader = PdfReader(file)
    text = "".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
    return text

# Function to create vector store
def create_vector_store(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = text_splitter.split_text(text)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    docsearch = FAISS.from_texts(texts, embeddings)
    
    return docsearch

# Function for voice recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        query_text = recognizer.recognize_google(audio)
        st.write(f"Recognized Question: {query_text}")
        return query_text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the speech."
    except sr.RequestError:
        return "Error with the speech recognition service."

# Function to read the answer in a separate thread
def speak_text(text):
    if text:
        st.session_state.is_speaking = True
        tts_engine.say(text)
        tts_engine.runAndWait()
        st.session_state.is_speaking = False  # Reset after speaking

# Stop speech function
def stop_speech():
    tts_engine.stop()
    st.session_state.is_speaking = False

if uploaded_file:
    document_text = load_document(uploaded_file)
    
    vector_store = create_vector_store(document_text)
    st.success("Document processed successfully!")

    # Load locally hosted Ollama model
    llm = Ollama(model="mistral")  
    qa_chain = load_qa_chain(llm, chain_type="stuff")

    # Get user input
    query = ""
    if mode == "Text":
        query = st.text_input("Ask a question about the document:")
    elif mode == "Voice":
        if st.button("🎤 Record Question"):
            query = recognize_speech()
            st.session_state["query"] = query  # Store query in session state
            #st.rerun()  # Force UI update after voice input

    if query:
        st.write("Searching for relevant document sections...")
        docs = vector_store.similarity_search(query)
        #st.write(f"Retrieved {len(docs)} relevant document chunks.")

        if len(docs) == 0:
            st.warning("No relevant sections found. Try rephrasing your question.")
        else:
            st.write("Generating answer...")
            st.session_state.answer = qa_chain.run(input_documents=docs, question=query)
            st.write("Answer:", st.session_state.answer)

# Buttons to read or stop the answer
col1, col2 = st.columns(2)

if st.session_state.answer:
    with col1:
        if st.button("🔊 Read Answer", key="read_btn"):
            if not st.session_state.is_speaking:
                # Start the thread without causing a refresh
                threading.Thread(target=speak_text, args=(st.session_state.answer,), daemon=True).start()
                st.session_state.is_speaking = True
                #st.rerun()  # Force UI update without breaking speech

    with col2:
        if st.button("⏹ Stop Reading", key="stop_btn"):
            stop_speech()
            st.rerun()  # Update UI state after stopping
