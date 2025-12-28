# Bengaluru RAG LLM Framework 🚀
An AI-powered Retrieval-Augmented Generation (RAG) system that answers Bengaluru-related queries using LangChain, FAISS, and HuggingFace models.


## ✨ Features
- Domain-specific RAG pipeline
- FAISS vector search
- Wikipedia-based knowledge retrieval
- Keyword guard for query filtering
- Streamlit-based web UI


## 🧠 Architecture
User Query  
→ Keyword Guard  
→ Vector Retrieval (FAISS)  
→ LLM Generation  
→ Streamlit UI


## 🛠 Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Transformers


## 🚀 Run Locally
pip install -r requirements.txt
streamlit run app.py


## 🌐 Live Demo
https://ckqddukklqdf5ivfz5izwf.streamlit.app/


## 📁 Project Structure
app.py
bengaluru_backend.py
bengaluru_guard.py
bengaluru_references.py
requirements.txt

