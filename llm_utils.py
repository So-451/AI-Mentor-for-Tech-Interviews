#Sets up your LLM + conversational chain.
from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationalRetrievalChain
from config import MODEL_NAME
from vectorstore import get_vectorstore

def get_conversation_chain():
    llm = ChatOllama(model=MODEL_NAME, temperature=0.2)
    vectordb = get_vectorstore()

    qa = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 4}),
        return_source_documents=True,
    )
    return qa
