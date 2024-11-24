from llama_index import VectorStoreIndex, ServiceContext
from llama_index.embeddings import SentenceTransformersEmbedding

def setup_query_engine(collection):
    """Setup LlamaIndex Query Engine."""
    embedding_service = SentenceTransformersEmbedding(model_name='all-MiniLM-L6-v2')
    service_context = ServiceContext.from_defaults(embed_model=embedding_service)
    return VectorStoreIndex.from_vector_store(collection, service_context=service_context).as_query_engine()
