#Holds constants and env vars so they’re reusable.
import os

PDF_PATH = "Cracking the Coding Interview.pdf"
DB_DIR = "./chroma_db"
MODEL_NAME = os.environ.get("OLLAMA_MODEL", "llama3")
REINDEX = os.environ.get("REINDEX", "0") == "1"
