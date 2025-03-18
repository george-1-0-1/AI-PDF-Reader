# AI-PDF-Reader
AI-powered document Q&amp;A assistant using Streamlit, LangChain, FAISS, and locally hosted Ollama LLM.

# AI PDF Reader with Voice and Text

##

- `app.py`: Original version supporting only text input.
- `appnew.py`: Enhanced version with voice input and text-to-speech featuresOverview

  This project is an AI-powered PDF reader that allows users to interact with documents via text or voice input. The application leverages local LLMs (such as Mistral) for answering questions based on the document content. It also features a text-to-speech (TTS) engine for reading responses aloud.
  ## Features
  - **Text-based interaction**: Users can type questions related to the uploaded PDF.
  - **Voice-based interaction**: Users can speak queries and receive spoken responses.
  - **Text-to-speech (TTS) support**: Answers can be read aloud.
  - **Local LLM support**: Uses an Ollama-hosted model (e.g., Mistral) for question answering.
  - **Vector search**: FAISS-based vector storage for efficient retrieval.
  ## Project Structure.

## Installation

To set up the project, follow these steps:

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/ai-pdf-reader.git
cd ai-pdf-reader
```

### 2. Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the Streamlit App

For the text-only version:

```sh
streamlit run app.py
```

For the voice-enabled version:

```sh
streamlit run appnew.py
```

## Dependencies

Make sure you have the following installed:

- `streamlit`
- `PyPDF2`
- `speechrecognition`
- `pyttsx3`
- `langchain`
- `faiss-cpu`
- `huggingface-hub`
- `ollama`


## Usage

1. Upload a PDF file.
2. Choose between text or voice input.
3. Ask questions about the document.
4. (Optional) Click "Read Answer" to hear the response.
5. (Optional) Click "Stop Reading" to stop the TTS output.

## Contributing

Feel free to open issues and pull requests to improve the project!

## License

[MIT License](LICENSE)

