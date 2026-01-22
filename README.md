📚 AI Document Reader Chatbot (Local RAG)

An AI-powered PDF document reader and chatbot built with Streamlit, ChromaDB, and Ollama.
It allows users to upload PDFs, extract content, perform semantic search, and ask questions using local LLMs — no cloud APIs required.

🚀 Features

📄 Upload and read PDF documents

🧠 Semantic chunking & vector storage (ChromaDB)

🔍 Context-aware question answering (RAG)

🧠 Runs fully locally using Ollama

🎙️ Text-to-speech support (gTTS)

🖥️ Simple & interactive Streamlit UI

🛠️ Tech Stack

Python 3.10+

Streamlit – UI

pypdf – PDF text extraction

ChromaDB – Vector database

Ollama – Local LLM inference

gTTS – Text-to-speech

📂 Project Structure
ai_doc_reader/
│
├── app_pro.py            # Main Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignored files (venv, cache, etc.)
└── venv/                 # Virtual environment (not pushed)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/deeju069-tech/Ai-Document-Reader-chatbot.git
cd Ai-Document-Reader-chatbot

2️⃣ Create & activate virtual environment
python -m venv venv


Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Start Ollama (required)

Make sure Ollama is running locally:

ollama serve


Pull a model if needed:

ollama pull llama3

5️⃣ Run the application
python -m streamlit run app_pro.py
