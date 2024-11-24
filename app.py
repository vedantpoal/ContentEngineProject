import streamlit as st
from src.document_parser import extract_text_from_pdf
from src.embeddings import generate_embeddings, store_embeddings, query_embeddings
from src.local_llm import query_local_llm

# Page title
st.title("Content Engine: PDF Comparison and Insights")

# File upload section
uploaded_files = st.file_uploader("Upload PDF Documents", type="pdf", accept_multiple_files=True)

if uploaded_files:
    documents = {file.name: extract_text_from_pdf(file) for file in uploaded_files}
    
    # Display document preview
    for name, content in documents.items():
        st.subheader(f"Preview of {name}")
        st.write(content[:500])  # Show a snippet of the document

    # Generate embeddings and store in ChromaDB
    if st.button("Generate Embeddings"):
        embeddings = generate_embeddings(documents)
        store_embeddings(embeddings, documents)
        st.success("Embeddings generated and stored successfully!")

# Query section
query = st.text_input("Ask a question about the uploaded documents:")
if query:
    # Query embeddings and LLM
    results = query_embeddings(query)
    llm_response = query_local_llm(query)
    st.subheader("Insights from Documents")
    st.write(results)
    st.subheader("Response from LLM")
    st.write(llm_response)
