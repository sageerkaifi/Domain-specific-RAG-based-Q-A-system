from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
from datetime import datetime
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

path = "indian-polity.pdf"
embeddings = OllamaEmbeddings(model="embeddinggemma:latest")
db_loc = "./chroma_langchain_db"

if os.path.exists(db_loc):
    print("[INFO] Existing Chroma DB found, loading retriever only.")
    db = Chroma(persist_directory=db_loc, embedding_function=embeddings)
else:
    print("[INFO] Creating new Chroma DB and embedding documents.")
    loader = PyPDFLoader(path)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(pages)
    for d in docs:
        d.metadata["filename"] = os.path.basename(path)
        d.metadata["uploaded_at"] = datetime.now().isoformat()
    db = Chroma.from_documents(docs, embeddings, persist_directory=db_loc)
    print(f"[INFO] DB saved at: {db_loc}")

retriver = db.as_retriever(
    search_kwargs={"k": 5}
)