# 📚 AI Document Reader – Local RAG System

An AI-powered **Document Question Answering system** that allows users to upload PDFs and ask questions using a **fully local Retrieval-Augmented Generation (RAG) pipeline** powered by **Ollama**, **ChromaDB**, and **Streamlit**.

No cloud APIs. No data leakage. 100% local AI.

---

## 🎯 Project Overview

This project enables users to:

- Upload PDF documents
- Automatically extract and chunk text
- Store embeddings in a local vector database (ChromaDB)
- Query the document using a local LLM (Ollama)
- Receive context-aware answers
- Optionally convert responses to speech (Text-to-Speech)

The system is ideal for **private documents**, **academic PDFs**, **resumes**, and **enterprise data** where privacy is critical.

---

## 🧠 System Architecture (Local RAG)

PDF Upload
↓
Text Extraction (PyPDF2 / pypdf)
↓
Chunking
↓
Embedding (Ollama)
↓
Vector Store (ChromaDB)
↓
Semantic Search
↓
LLM Answer Generation (Ollama)
↓
Optional Audio Output (gTTS)


---

## 🛠️ Technology Stack

- **Frontend:** Streamlit  
- **LLM:** Ollama (LLaMA 3 / compatible models)  
- **Vector Database:** ChromaDB (Persistent)  
- **PDF Processing:** PyPDF2 / pypdf  
- **Text-to-Speech:** gTTS  
- **Language:** Python 3.10+  

---

## 📁 Project Structure

ai_doc_reader/
├── app_pro.py # Main Streamlit application
├── vectordb/ # Persistent ChromaDB storage
├── requirements.txt
├── README.md
├── .gitignore
└── venv/


---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

---
git clone https://github.com/yourusername/ai-doc-reader.git
cd ai-doc-reader
---
### 2️⃣ Create a virtual environment
python -m venv venv

Activate it 

venv\Scripts\activate
---
### 3️⃣ Install dependencies

pip install -r requirements.txt
---
### 4️⃣ Install & start Ollama

Download Ollama from https://ollama.com

Pull a model:

ollama pull llama3

Start Ollama server:

ollama serve
---
### 💻 Usage
---
Web Interface (Streamlit)

streamlit run app_pro.py
---
