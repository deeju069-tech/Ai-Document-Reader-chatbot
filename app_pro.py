import streamlit as st
import PyPDF2
import ollama
import chromadb
from gtts import gTTS
import io

# --- Configuration ---
st.set_page_config(page_title="Pro Local RAG", layout="wide", page_icon="💾")
st.title("💾 Dhee Ai Chatbot")

# Initialize ChromaDB in Persistent Mode (Optional)
if 'collection' not in st.session_state:
    client = chromadb.Client()
    # Unique name to avoid conflicts
    st.session_state.collection = client.get_or_create_collection(name="user_documents")

# --- Helper Logic ---

def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"
    return text

def get_summary(text):
    """Generates a concise summary using the LLM."""
    prompt = f"Summarize the following document content in 3-5 bullet points focusing on key themes:\n\n{text[:3000]}"
    try:
        response = ollama.chat(model="tinyllama", messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except:
        return "Summary unavailable."

# --- Sidebar: Ingestion ---
with st.sidebar:
    st.header("📂 Document Input")
    uploaded_file = st.file_uploader("Upload a PDF (Resume, Tech Doc, etc.)", type=["pdf"])
    
    if uploaded_file:
        # Check if we've already processed THIS specific file
        if "last_uploaded" not in st.session_state or st.session_state.last_uploaded != uploaded_file.name:
            with st.spinner("Processing document..."):
                raw_text = extract_text(uploaded_file)
                st.session_state.full_text = raw_text
                
                # Semantic Chunking (Smaller chunks for better accuracy in small models)
                chunks = [raw_text[i:i+800] for i in range(0, len(raw_text), 600)]
                
                # Clear old data and add new
                ids = [f"id_{i}" for i in range(len(chunks))]
                embeddings = [ollama.embeddings(model="nomic-embed-text", prompt=c)["embedding"] for c in chunks]
                
                st.session_state.collection.add(
                    ids=ids,
                    embeddings=embeddings,
                    documents=chunks,
                    metadatas=[{"source": uploaded_file.name}] * len(chunks)
                )
                
                st.session_state.summary = get_summary(raw_text)
                st.session_state.last_uploaded = uploaded_file.name
                st.success("Indexing Complete!")

    if "summary" in st.session_state:
        st.info(f"📋 **File Summary:**\n{st.session_state.summary}")
    
    if st.button("Clear Session"):
        st.session_state.clear()
        st.rerun()

# --- Main Chat ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_query := st.chat_input("Ask about your document:"):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # 1. Retrieval
            q_emb = ollama.embeddings(model="nomic-embed-text", prompt=user_query)["embedding"]
            results = st.session_state.collection.query(query_embeddings=[q_emb], n_results=3)
            context_text = "\n\n".join(results["documents"][0])

            # 2. Dynamic System Prompt
            # We don't hardcode "SQL" here so it works for resumes or any PDF.
            messages = [
                {
                    "role": "system",
                    "content": f"""You are a precise technical assistant. 
                    Use the PROVIDED CONTEXT to answer the user's question. 
                    If the answer isn't in the context, use your general knowledge but clearly state 'According to my general knowledge...'
                    
                    CONTEXT FROM UPLOADED FILE:
                    {context_text}"""
                },
                {"role": "user", "content": user_query}
            ]

            response = ollama.chat(model="tinyllama", messages=messages)
            answer = response['message']['content'].strip()
            
            st.markdown(answer)
            
            # 3. Audio Handover
            try:
                tts = gTTS(text=answer[:300], lang='en')
                audio_io = io.BytesIO()
                tts.write_to_fp(audio_io)
                st.audio(audio_io)
            except:
                pass

    st.session_state.messages.append({"role": "assistant", "content": answer})
    