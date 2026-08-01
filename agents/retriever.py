from utils.embeddings import get_embedding_model
from langchain_chroma import Chroma

embedding_model = get_embedding_model()

vector_db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding_model
)

retriever = vector_db.as_retriever(
    search_kwargs={"k":3}
)


def retrieve(query):
    return retriever.invoke(query)