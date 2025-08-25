#Handles embedding + ChromaDB.
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from config import PDF_PATH, DB_DIR, REINDEX
from pdf_utils import load_pdf_as_documents


def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    if REINDEX or not os.path.exists(DB_DIR) or not os.listdir(DB_DIR):
        print("[Index] Building ChromaDB from PDF…")
        base_docs = load_pdf_as_documents(PDF_PATH)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(base_docs)
        vectordb = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=DB_DIR)
        vectordb.persist()
    else:
        print("[Index] Using existing ChromaDB.")
        vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    return vectordb
