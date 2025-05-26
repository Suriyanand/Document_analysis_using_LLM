import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

import google.generativeai as genai
import os

# Set your Gemini API key (make sure it's in your environment or paste it directly)
genai.configure(api_key="AIzaSyCGJ-Pipi8Jke1wjg1EZ2Aj-4q9epO7evc")

# Setup embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

st.title("🤖 Document Chatbot using Gemini + Chroma")

# Upload file
uploaded_file = st.file_uploader("📄 Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    # Save file temporarily
    file_path = "temp.txt"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load document
    loader = TextLoader(file_path)
    docs = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    # Create Chroma VectorStore
    persist_dir = "chroma_db"
    vectorstore = Chroma.from_documents(
        documents=split_docs,
        embedding=embedding_model,
        persist_directory=persist_dir
    )
    vectorstore.persist()
    st.success("✅ Document embedded and stored successfully!")

    # Ask a question
    query = st.text_input("💬 Ask a question about the document")

    if query:
        # Retrieve top 3 similar chunks
        results = vectorstore.similarity_search(query, k=3)

        # Combine context for Gemini
        context = "\n\n".join([res.page_content for res in results])

        # Run Gemini model
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(f"Answer this question: {query}\n\nUsing the following context:\n{context}")

        # Display result
        st.subheader("🧠 Gemini Answer:")
        st.write(response.text)

        # Optionally show the context
        with st.expander("🔍 View Retrieved Context Chunks"):
            for i, res in enumerate(results):
                st.markdown(f"**Chunk {i+1}:** {res.page_content}")
