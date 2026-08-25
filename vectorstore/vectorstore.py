from langchain_chroma import Chroma
from utils.embeddings import get_embedding_model


CHROMA_PATH = "database/chroma"


def create_vectorstore(chunks, embedding_model):

    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )


def load_vectorstore():

    embeddings = get_embedding_model()

    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )