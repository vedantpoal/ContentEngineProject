Content Engine with Document Comparison and Insights
Overview
This Content Engine is designed to process, compare, and analyze multiple PDF documents using Retrieval Augmented Generation (RAG) techniques. Specifically, the system processes Form 10-K filings of multinational companies (Alphabet, Tesla, and Uber), extracts content, and allows users to query and compare information from the documents. The backend is powered by LlamaIndex and ChromaDB for vector storage, and the frontend is built using Streamlit for interactive user interfaces. The system integrates a locally running Large Language Model (LLM) via Ollama for generating insights from the document content.

Project Structure
The project consists of the following components:

Backend:
Document Processing: Extracts content from PDF files.
Vector Generation: Converts document content into vector embeddings.
Database (ChromaDB): Stores and retrieves document embeddings.
LLM Integration: Uses a locally running Ollama LLM to generate contextual insights from the documents.
Frontend:
Streamlit App: Provides a user-friendly interface for querying documents and comparing information.
Installation
Prerequisites
Make sure the following tools are installed:

Python 3.8+: Ensure Python is installed.
Ollama: Install Ollama for running local LLMs.
Ollama Installation Guide
ChromaDB: Python client for vector storage.
Install via pip install chromadb
LlamaIndex: Install via pip install llama_index
Streamlit: Install via pip install streamlit
PyPDF2: Install via pip install PyPDF2
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/content-engine.git
cd content-engine
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Setting Up Ollama
Run the Ollama server locally:

bash
Copy code
ollama serve
Test the server by querying available models:

bash
Copy code
curl http://localhost:11434/models
Ensure that the server is running and accessible at http://localhost:11434.

Set Up ChromaDB
ChromaDB will automatically initialize when the backend is first run, creating the necessary directories and collections.
Ensure the persist_directory is set correctly in client = chromadb.Client(Settings(persist_directory="./embeddings/chroma_store")).
Running the Application
To run the Streamlit app, execute the following command:

bash
Copy code
streamlit run app.py
This will start the Streamlit server and you can access the frontend by navigating to http://localhost:8501 in your web browser.

Usage
Features
Document Comparison:

Upload and analyze the three Form 10-K filings (Alphabet, Tesla, Uber).
Compare and contrast the content across these documents.
Question-Answering Interface:

Ask specific questions related to the documents such as:
"What are the risk factors associated with Google and Tesla?"
"What is the total revenue for Google Search?"
"What are the differences in the business of Tesla and Uber?"
Insights Generation:

The system uses the locally running LLM to generate insights from the documents based on user queries.
Example Queries
Risk Factors: "What are the risk factors associated with Google and Tesla?"
Revenue Information: "What is the total revenue for Google Search?"
Business Comparison: "What are the differences in the business of Tesla and Uber?"
System Architecture
The system operates with the following architecture:

PDF Extraction: The documents are parsed to extract the text content.
Vector Generation: Using a local embedding model, the extracted text is converted into vector representations.
Vector Storage: The embeddings are stored in a ChromaDB collection for fast retrieval and querying.
LLM Integration: The query engine fetches relevant document segments and feeds them to a local LLM (via Ollama) for generating insights.
Frontend: The Streamlit app allows users to interact with the system via a chatbot-like interface.
Project Workflow
Initialize ChromaDB: When the application starts, ChromaDB is initialized, creating a directory for storing embeddings.
Document Parsing: PDF documents (Form 10-K filings) are parsed and processed to extract relevant content.
Embedding Generation: Text content is converted into embeddings using a local model.
Embedding Storage: The embeddings are stored in ChromaDB for querying.
Query Handling: The user queries are processed using the vector search engine, retrieving relevant embeddings and using the local LLM to generate insights.
