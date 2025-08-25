#Chat function used by Gradio.
import os
from langchain.schema import HumanMessage, AIMessage
from llm_utils import get_conversation_chain


qa = get_conversation_chain()

def chat_fn(message, history):
    try:
        lc_history = []
        for user_msg, bot_msg in history:
            lc_history.append(HumanMessage(content=user_msg))
            lc_history.append(AIMessage(content=bot_msg))

        lc_history.append(HumanMessage(content=message))

        result = qa.invoke({"question": message, "chat_history": lc_history})
        answer = result.get("answer", "")

        new_history = history + [[f"🧑 {message}", f"🤖 {answer}"]]
        return new_history, new_history
    except Exception as e:
        print("chat_fn error:", e)
        return history + [["Error", "Sorry, something went wrong."]], history
# ----------------- GRADIO BLOCKS APP -----------------