#Contains only UI (Gradio Blocks).
import gradio as gr
from chat_handler import chat_fn


TITLE = "🤖 AI Mentor for Technical Interviews"
DESC = "Let this AI Mentor assist you in preparing for technical interviews."

def create_ui():
    with gr.Blocks(css=""" #chatbox-row {
        display: flex;
        align-items: center;
        padding: 10px;
        background-color: #1e1e1e;
        border-top: 1px solid #333;
        position: sticky;
        bottom: 0;
        z-index: 100;
    }

    #user-msg {
        flex-grow: 1;
        border-radius: 8px;
        padding: 8px;
        margin-right: 8px;
        font-size: 16px;
        resize: none !important;
        overflow-y: auto !important;
    }

    #submit-btn {
        all: unset;                 /* reset default gradio button styles */
        display: inline-flex;       /* don’t stretch */
        align-items: center;
        justify-content: center;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background-color: #2d3748;
        color: white;
        font-size: 18px;
        cursor: pointer;
        transition: background 0.2s;
    }
    #submit-btn:hover {
        background-color: #4a5568;
    } """) as demo:
        gr.Markdown(f"# {TITLE}")
        gr.Markdown(DESC)

        chatbot = gr.Chatbot()
        state = gr.State([])

        with gr.Row(elem_id="chatbox-row"):
            msg = gr.Textbox(
                placeholder="e.g., Explain KMP algorithm. Or Quiz me on arrays",
                elem_id="user-msg",
                show_label=False,
                lines=1,
                max_lines=6,
            )
            submit_btn = gr.Button("➤", elem_id="submit-btn")

        submit_btn.click(chat_fn, inputs=[msg, state], outputs=[chatbot, state])
        msg.submit(chat_fn, inputs=[msg, state], outputs=[chatbot, state])

    return demo
