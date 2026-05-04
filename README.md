# 📄 MultiPDF Chat App

An interactive AI-powered application that lets you **chat with multiple PDF documents at once**. Ask questions in natural language and get precise, context-aware answers strictly grounded in the uploaded PDFs.

<img width="2816" height="1536" alt="SmartDoc QandA" src="https://github.com/user-attachments/assets/a08ccf0a-9522-4661-b860-5e9ced142cf8" />

---

## 🚀 Overview

The **MultiPDF Chat App** uses modern NLP techniques and large language models to turn static PDF documents into an intelligent, conversational knowledge base. Instead of manually searching through pages, you simply ask questions — the app finds relevant sections and generates accurate responses.

Key promise: **No hallucinations outside the PDFs.** If the answer isn’t in the documents, the app won’t invent one.

---


## 🧠 How It Works

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

3. **Set up environment variables (Optional)**
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

