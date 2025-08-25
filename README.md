# DocuMind-AI-RAG-Application
DocuMind AI is a powerful and privacy-focused application designed to transform how you interact with PDF documents.It is built using Streamlit interface, which allows to engage in conversational Q&amp;A sessions directly with your files, eliminating the need for manual searching.The project employs a Retrieval-Augmented Generation (RAG) architecture. 

# Introduction
DocuMind AI is a powerful and privacy-focused application designed to transform how you interact with PDF documents. Built with a user-friendly Streamlit interface, this tool allows you to engage in conversational Q&A sessions directly with your files, eliminating the need for manual searching. At its core, the project employs a Retrieval-Augmented Generation (RAG) architecture. Upon uploading a PDF, the system processes its content, converting text into numerical representations stored within a local vector database. This enables an AI agent to perform rapid, semantic retrieval of the most relevant information when you ask a question. Leveraging Ollama, the application runs large language models (LLMs) and agentic workflows entirely on your local machine, guaranteeing that your documents and queries remain completely private. By grounding its responses in the context retrieved from the vector database, the AI provides precise, accurate answers, making it an ideal solution for students, researchers, and professionals who need to efficiently extract insights without compromising data confidentiality.

# 🚀 Demo
https://drive.google.com/file/d/1912Dhe5XfvH7TyMv5C7am-BYvXrrrf69/view?usp=sharing

# ✨ Features
Interactive Chat Interface: Ask questions in natural language and receive conversational answers.
Powered by Local LLMs: Integrates with Ollama to run various open-source models (e.g., Llama3, Mistral) locally.
Privacy-First: Your documents and queries never leave your machine.
High Accuracy with RAG: Provides answers grounded in the PDF's content, reducing AI hallucinations.
Efficient Search: Uses a vector database for fast, semantic retrieval of relevant context.
Agentic Workflows: Utilizes agentic capabilities of LLMs for better query understanding.

# ⚙️ Tech Stack
Frontend: Streamlit
LLM Serving: Ollama
AI Architecture: Retrieval-Augmented Generation (RAG)
Vector Database: ChromaDB 
Embeddings: Sentence-Transformers
Orchestration: LangChain / LlamaIndex (Mention which one you used)
Language: Python

# 🛠️ How It Works
The project follows a classic RAG pipeline:

1)PDF Ingestion & Chunking: The user uploads a PDF. The document is parsed and split into smaller, manageable text chunks.
2)Embedding Generation: Each text chunk is converted into a numerical vector (embedding) that captures its semantic meaning.
3)Vector Storage: These embeddings are indexed and stored in a local vector database. This creates a searchable knowledge base from the document.
4)User Query & Retrieval: When a user asks a question, it's also converted into an embedding. The vector database is then queried to find the most similar (i.e., most relevant) text chunks from the document.
5)Context Augmentation: The retrieved text chunks (the context) are combined with the user's original question into a detailed prompt.
6)LLM Generation: This augmented prompt is sent to the LLM running via Ollama. The model uses the provided context to generate a relevant and accurate answer.
7)Display Answer: The final answer is streamed back to the user in the Streamlit chat interface.

# 🔧 Getting Started
Prerequisites
Python 3.9+
Ollama: Ensure  is installed and running.
Pull the LLM model you wish to use.

# Installation
Clone the repository:
Create and activate a virtual environment:
Install dependencies:
Run the application:
Navigate to http://localhost:8501 in your browser to start using the app.
