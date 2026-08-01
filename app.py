from utils.loader import load_pdf

docs = load_pdf("data/pdfs/sample.pdf")

print(f"Pages Loaded : {len(docs)}")

print("-" * 60)

print(docs[0].page_content[:500])

print("-" * 60)

print(docs[0].metadata)



#---------------------------------------#
#---------SPLITTER--------------------------#

from utils.loader import load_pdf
from utils.splitter import split_documents

docs = load_pdf("data/pdfs/sample.pdf")

chunks = split_documents(docs)

print("Pages :", len(docs))
print("Chunks:", len(chunks))

print("-" * 60)

print(chunks[0].page_content)

print("-" * 60)

print(chunks[0].metadata)



#---------------------------------------#
#---------EMBEDDINGS--------------------------#

from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model

# 1. Load PDF
docs = load_pdf("data/pdfs/sample.pdf")

# 2. Split Documents
chunks = split_documents(docs)

# 3. Get Embedding Model
embeddings = get_embedding_model()

# Test embedding on first chunk
vector = embeddings.embed_query(chunks[0].page_content)
from vectorstore.vectorstore import create_vectorstore

vector_db = create_vectorstore(
    chunks,
    embeddings
)

print("Vector Dimension:", len(vector))
print("First 10 values:", vector[:10])

retriever = vector_db.as_retriever(
    search_kwargs={"k":3}
)

results = retriever.invoke(
    "What is Artificial Intelligence?"
)

for i, doc in enumerate(results):

    print("="*50)

    print("Result", i+1)

    print(doc.page_content[:400])

print(results[0].metadata)


from agents.retriever import retrieve
from agents.generator import generate_answer

query = input("Ask a question: ")

documents = retrieve(query)

answer = generate_answer(
    query,
    documents
)

print("\nAnswer:\n")
print(answer)