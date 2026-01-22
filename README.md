# 📄 MultiPDF Chat App

An interactive AI-powered application that lets you **chat with multiple PDF documents at once**. Ask questions in natural language and get precise, context-aware answers strictly grounded in the uploaded PDFs.

This project is built for learning and experimentation, and accompanies a step-by-step YouTube tutorial.

---

## 🚀 Overview

The **MultiPDF Chat App** uses modern NLP techniques and large language models to turn static PDF documents into an intelligent, conversational knowledge base. Instead of manually searching through pages, you simply ask questions — the app finds relevant sections and generates accurate responses.

Key promise: **No hallucinations outside the PDFs.** If the answer isn’t in the documents, the app won’t invent one.

---

## 🧠 How It Works

![Architecture Diagram](./docs/PDF-LangChain.jpg)

The application follows a Retrieval-Augmented Generation (RAG) pipeline:

1. **PDF Ingestion**
   Multiple PDF files are loaded and their textual content is extracted.

2. **Text Chunking**
   The extracted text is split into smaller, overlapping chunks to preserve context while staying within model limits.

3. **Embedding Generation**
   Each text chunk is converted into a numerical vector (embedding) using a language model.

4. **Semantic Search**
   When a user asks a question, its embedding is compared with document embeddings to find the most relevant chunks.

5. **Answer Generation**
   The most relevant chunks are passed to the language model, which formulates a clear and grounded response.

---

## ✨ Features

* 📚 Chat with **multiple PDFs simultaneously**
* 🔍 Semantic search for highly relevant answers
* 🤖 LLM-powered responses grounded in document content
* 🧠 Context-aware chunking for better accuracy
* 🌐 Clean and simple **Streamlit-based UI**

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Web interface
* **LangChain** – Document processing & retrieval pipeline
* **OpenAI API** – Embeddings and language model
* **FAISS / Vector Store** – Similarity search

---

## 📦 Installation

Follow these steps to run the project locally:

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd multipdf-chat-app
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_secret_api_key
   ```

---

## ▶️ Usage

1. Start the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. The app will open automatically in your default browser.

3. Upload one or more PDF files using the sidebar.

4. Ask questions in natural language using the chat interface.

5. Receive answers based **only** on the uploaded documents.

---

## 📺 Tutorial

This project is based on a YouTube walkthrough that explains the complete build process:

👉 **Watch here:** [https://youtu.be/dXxQ0LR-3Hg](https://youtu.be/dXxQ0LR-3Hg)

---

## 🎯 Use Cases

* Research paper analysis
* Studying technical documentation
* Legal or policy document Q&A
* Academic notes and textbooks
* Internal company knowledge bases

---

## ⚠️ Limitations

* Answers are limited to the content present in the uploaded PDFs
* Performance depends on document quality and chunking strategy
* Requires an active OpenAI API key

---

## 📄 License & Contributions

This repository is intended **strictly for educational purposes** and serves as supporting material for the YouTube tutorial. External contributions are not accepted.

You are encouraged to fork the project, modify it, and extend it for your own learning or experimentation.

---

## 🌱 Future Enhancements (Ideas)

* Support for other file formats (DOCX, TXT)
* Chat history persistence
* Source citation for each answer
* Multi-user authentication
* Local LLM support

---

Happy hacking. PDFs don’t have to be silent anymore.
