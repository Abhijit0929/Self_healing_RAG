from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model
from vectorstore.vectorstore import create_vectorstore

print("Loading PDF...")

docs = load_pdf("data/pdfs/sample.pdf")

print(f"Loaded {len(docs)} pages.")

chunks = split_documents(docs)

print(f"Created {len(chunks)} chunks.")

embeddings = get_embedding_model()

print("Generating embeddings and creating vector database...")

create_vectorstore(chunks, embeddings)

print("✅ Ingestion completed successfully.")