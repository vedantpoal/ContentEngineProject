from sentence_transformers import SentenceTransformer
from chromadb import Client
from chromadb.config import Settings

# Initialize model and vector store
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
client = Client(Settings(persist_directory="./embeddings/chroma_store"))

def generate_embeddings(documents):
    """Generate embeddings for document content."""
    return {
        name: embedding_model.encode(content.split("\n"))  # Split into sentences
        for name, content in documents.items()
    }

def store_embeddings(embeddings, documents):
    """Store embeddings in ChromaDB."""
    collection = client.create_collection("document_embeddings")
    for doc_name, embedding in embeddings.items():
        collection.add(
            embeddings=embedding,
            documents=documents[doc_name].split("\n"),
            metadatas=[{"document": doc_name}] * len(embedding)
        )

def query_embeddings(query):
    """Query embeddings from ChromaDB."""
    collection = client.get_collection("document_embeddings")
    results = collection.query(query_embeddings=[embedding_model.encode(query)], n_results=5)
    return results
