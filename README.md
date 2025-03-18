# AI PDF Reader with Voice and Text

AI-powered document Q&amp;A assistant using Streamlit, LangChain, FAISS, and locally hosted Ollama LLM.

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
git clone https://github.com/george-1-0-1/AI-PDF-Reader.git
cd AI-PDF-Reader
```

### 2. Installing Ollama and pulling Mistral

```sh
ollama pull mistral
```

### 3. Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 4. Install Dependencies

```sh
pip install -r requirements.txt
```

### 5. Run the Streamlit App

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


## Troubleshooting

- **TTS not working or crashes the app?** Make sure `pyttsx3` is installed and working.
- **Streamlit app refreshing unexpectedly?** Avoid using `st.experimental_rerun()`, as it may cause issues.
- **Ollama Model Not Found?** Ensure you've pulled the correct model with `ollama pull mistral`.

## Contributing

Feel free to open issues and pull requests to improve the project!

## License

[MIT License](LICENSE)
