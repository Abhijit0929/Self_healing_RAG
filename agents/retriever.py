from vectorstore.vectorstore import load_vectorstore

vector_db = load_vectorstore()

retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

def retrieve(query):
    return retriever.invoke(query)