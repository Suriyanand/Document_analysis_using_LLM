Document Chatbot Using Gemini + Chroma
A Streamlit app that lets you upload .txt documents, embed them using LangChain + Chroma, and chat with the document using Gemini (Google’s generative AI).

Features
Upload .txt files (up to 200MB)

Document embedding with LangChain + Chroma vector store

Ask questions about the uploaded document

Responses powered by Google Gemini LLM

Simple and intuitive UI with Streamlit

How to Run Locally
bash
Copy
Edit
# Clone repo
git clone https://github.com/your-username/document-analysis-llm.git
cd document-analysis-llm

# Create virtual env & activate
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
Open the local URL in your browser and start uploading documents!

Deployment
You can deploy this app easily on Streamlit Cloud:

Push your code to GitHub.

Connect your repo on Streamlit Cloud.

Set main file path to app.py.

Deploy and share your app URL.




Notes
Requires a Google API key for Gemini. Set it as an environment variable GENAI_API_KEY.

Supports .txt files only.

Max file size: 200MB

License
MIT License © 2025 YourName
