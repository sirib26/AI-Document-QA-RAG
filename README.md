# AI Document Q&A System (RAG-based)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based system that allows users to upload a document and ask questions. The system retrieves relevant information from the document and generates accurate, context-aware answers using a local language model.

---

## How It Works

1. Document Loading
   Loads PDF documents using LangChain loaders

2. Text Chunking
   Splits the document into smaller chunks for efficient processing

3. Embeddings Generation
   Converts text into vector embeddings using HuggingFace models

4. Vector Storage (FAISS)
   Stores embeddings for fast similarity search

5. Retrieval
   Finds the most relevant chunks based on user query

6. Answer Generation (LLM)
   Uses TinyLlama (via Ollama) to generate answers from retrieved context

---

## Tech Stack

* Python
* LangChain
* FAISS
* HuggingFace Embeddings
* Ollama (TinyLlama - Local LLM)
* FastAPI (Backend)
* Streamlit (Frontend UI)

---

## Project Structure

```
AI-QA/
│
├── app.py              # FastAPI backend
├── rag.py              # Core RAG pipeline
├── ui.py               # Streamlit UI
├── sample.pdf          # Sample document
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/AI-Document-QA-RAG.git
cd AI-Document-QA-RAG
```

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Install Ollama and pull model

```
ollama pull tinyllama
```

---

## Run the Application

### Run Backend (FastAPI)

```
uvicorn app:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

### Run Frontend (Streamlit)

```
streamlit run ui.py
```

---

## Example Usage

* Ask: What is Artificial Intelligence?
* Output: AI-generated answer based on document content

---

## Features

* Document-based question answering
* Semantic search using FAISS
* Context-aware response generation
* FastAPI backend for API access
* Interactive Streamlit UI
* Fully local execution (no paid APIs required)

---

## Future Improvements

* Support for multiple documents
* Chat history memory
* Source highlighting
* Cloud deployment

---

## Author

Siri B
B.E Computer Science Engineering

---

## Acknowledgements

* LangChain
* HuggingFace
* Ollama

---

If you found this project useful, consider starring the repository.
