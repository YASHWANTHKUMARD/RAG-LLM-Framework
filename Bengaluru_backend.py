from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

# -----------------------------
# LOAD WIKIPEDIA DATA
# -----------------------------
loader = WikipediaLoader(
    query="Bengaluru",
    load_max_docs=5
)
docs = loader.load()

# -----------------------------
# SPLIT TEXT
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=30
)
chunks = splitter.split_documents(docs)

# -----------------------------
# EMBEDDINGS + FAISS
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
db = FAISS.from_documents(chunks, embeddings)
retriever = db.as_retriever(search_kwargs={"k": 2})

# -----------------------------
# LOAD LLM
# -----------------------------
pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct",
    max_new_tokens=256,
    temperature=0.2
)
llm = HuggingFacePipeline(pipeline=pipe)

# -----------------------------
# RAG FUNCTION (PURE)
# -----------------------------
def rag_chain(question):
    docs = retriever.invoke(question)

    if not docs:
        return None

    if len(docs[0].page_content.strip()) < 50:
        return None

    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
You are Bengaluru AI.
Answer ONLY using the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question: {question}
Answer:
"""
    response = llm.invoke(prompt)
    return response.replace(prompt, "").strip()
