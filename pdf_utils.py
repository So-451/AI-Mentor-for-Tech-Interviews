#For PDF → documents.
import pdfplumber
from typing import List
from langchain.docstore.document import Document

def load_pdf_as_documents(pdf_path: str) -> List[Document]:
    docs = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            text = text.strip()
            if text:
                docs.append(Document(page_content=text, metadata={"source": pdf_path, "page": i+1}))
    return docs
