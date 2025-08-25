# 🤖 AI Mentor for Technical Interviews

**AI Mentor** is an interactive assistant designed to help users prepare for DSA (Data Structures & Algorithms) and coding interviews. It leverages semantic search over your notes and provides clear explanations, code snippets, and insights in a chat interface.

---

## 🚀 Key Features

- Conversational AI to answer technical questions.
- Semantic search over your PDF notes (e.g., *Cracking the Coding Interview*).
- Syntax-highlighted code snippets in responses.
- Step-by-step explanations for tricky DSA problems.
- Tracks session history for ongoing learning.
- Handles multiple topics: arrays, strings, recursion, graphs, dynamic programming, etc.

---

## 🧩 Tricky Sample Questions

To showcase the AI Mentor in action:

- **Two Sum Problem** – Find indices of two numbers that sum to a target.
- **Maximum Subarray (Kadane’s Algorithm)** – Find the largest sum of contiguous subarray.
- **KMP Algorithm** – Pattern matching in strings.
- **Graph Traversal** – BFS/DFS questions for shortest paths or connectivity.
- **Dynamic Programming** – Classic problems like Coin Change, Longest Increasing Subsequence.

---

## 🛠 Tech Stack

- **Backend & LLM**: LangChain, Ollama (using **llama3** model)
- **Vector Store**: Chroma + HuggingFace Embeddings
- **PDF Parsing**: pdfplumber
- **Frontend**: Gradio (Blocks & Chatbot)

---

## 💻 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/So_451/AI_Mentor.git
cd AI_Mentor
```

2. **Create a virtual environment**:

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/macOS
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the app**:

```bash
python mentor.py
```

5. **Open the app** in your browser at the URL provided by Gradio (usually `http://127.0.0.1:7860`).

---

## 📂 Project Structure

```
AI_Mentor/
├── mentor.py          # Main app
├── chat_handler.py    # Handles chat logic
├── llm_utils.py       # LLM helper functions
├── vectorstore.py     # Chroma DB helper
├── pdf_utils.py       # PDF loader
├── requirements.txt   # Python dependencies
├── .gitignore         # Ignore virtual environment, data, etc.
└── README.md          # Project overview
```

---

## ⚡ Usage

1. Launch the app.
2. Ask questions like:
   - "Explain Two Sum problem."
   - "Quiz me on graphs."
3. The AI responds with grounded explanations, code snippets, and references.

---



## 🌟 Future Improvements

- Dockerize for easy deployment.
- Deploy to HuggingFace Spaces for a permanent public link.
- Add “Step-by-Step Hints” mode.
- Expand topic coverage to advanced algorithms and system design.

---

## 📄 License

MIT License © 2025

