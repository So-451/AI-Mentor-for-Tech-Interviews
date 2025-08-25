from ui import create_ui

if __name__ == "__main__":
    demo = create_ui()
    demo.launch(share=True)

'''
To activate virtual environment
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\\.venv\\Scripts\\Activate.ps1

docker run -p 7860:7860 ai-mentor
ngrok http 7860


''' 

