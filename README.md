# 📄 Smart AI PDF Analyzer

An AI-powered Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and interact with them using natural language. The system leverages semantic search, vector embeddings, and a locally hosted Large Language Model (LLM) to deliver context-aware answers.

---

## 🚀 Features

- 📂 Upload and analyze PDF documents
- 🧠 Semantic search using HuggingFace Sentence Transformers
- ⚡ Fast similarity search with FAISS vector indexing
- 🤖 Local AI inference using Ollama (Mistral)
- 💬 Interactive chat interface built with Streamlit
- 📊 Document insights including chunk count and character statistics
- 🔍 Retrieval-Augmented Generation (RAG) pipeline for accurate responses

---

## 🏗️ Architecture

```
                  PDF Document
                        │
                        ▼
             Text Extraction (pdfplumber)
                        │
                        ▼
                 Text Chunking
                        │
                        ▼
      HuggingFace Sentence Embeddings
                        │
                        ▼
              FAISS Vector Database
                        │
                        ▼
         Semantic Similarity Retrieval
                        │
                        ▼
            Ollama (Mistral Local LLM)
                        │
                        ▼
            Context-Aware AI Response
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama
- Mistral
- HuggingFace Sentence Transformers
- FAISS
- pdfplumber
- NumPy

---

## 📂 Project Structure

```
smart-ai-pdf-analyzer/
│
├── app/
│   ├── pdf_utils.py
│   ├── text_utils.py
│   ├── hf_embeddings.py
│   ├── vector_store.py
│   ├── ollama_chat.py
│   ├── rag_pipeline.py
│
├── streamlit_app.py
├── sample.pdf
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-ai-pdf-analyzer.git

cd smart-ai-pdf-analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the Mistral model:

```bash
ollama pull mistral
```

Start Ollama:

```bash
ollama run mistral
```

---

## ▶️ Run the Application

Open another terminal and run:

```bash
streamlit run streamlit_app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 💡 How It Works

1. Upload a PDF document.
2. Extract text using **pdfplumber**.
3. Split the text into manageable chunks.
4. Generate vector embeddings using **HuggingFace Sentence Transformers**.
5. Store embeddings in a **FAISS** vector index.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant chunks using semantic similarity.
8. Pass the retrieved context to **Ollama (Mistral)**.
9. Generate a context-aware response.

---



## 🎯 Future Improvements

- Multi-PDF support
- PostgreSQL + pgvector integration
- Chat history persistence
- Source citations for retrieved chunks
- Document summarization
- PDF highlighting of referenced sections
- Docker support
- Cloud deployment
