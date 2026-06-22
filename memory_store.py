import os
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings


DB_PATH = "faiss_index"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def load_db():
    if os.path.exists(DB_PATH):
        return FAISS.load_local(
            DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    db = FAISS.from_documents(
        [Document(page_content="Memory initialized")],
        embeddings
    )
    db.save_local(DB_PATH)
    return db

def save_memory(text):
    db = load_db()
    db.add_documents([Document(page_content=text)])
    db.save_local(DB_PATH)

def search_memory(query):
    db = load_db()
    docs = db.similarity_search(query, k=3)
    return [doc.page_content for doc in docs]