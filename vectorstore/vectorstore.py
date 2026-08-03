from langchain_chroma import Chroma
from utils.embeddings import get_embedding_model


def create_vectorstore(chunks, embedding_model):

    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="vectorstore"
    )


def load_vectorstore():

    embeddings = get_embedding_model()

    return Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )