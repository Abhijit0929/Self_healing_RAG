from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model
from vectorstore.vectorstore import create_vectorstore


print("=" * 60)
print("DOCUMENT INGESTION")
print("=" * 60)

print("\nLoading PDF...")

docs = load_pdf("data/pdfs/sample.pdf")

print(f"Pages loaded: {len(docs)}")

print("\nSplitting documents...")

chunks = split_documents(docs)

print(f"Chunks created: {len(chunks)}")

print("\nLoading embedding model...")

embeddings = get_embedding_model()

print("\nCreating vector database...")

create_vectorstore(
    chunks,
    embeddings
)

print("\n" + "=" * 60)
print("✅ INGESTION COMPLETED")
print("=" * 60)