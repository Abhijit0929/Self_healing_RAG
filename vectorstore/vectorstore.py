from langchain_chroma import Chroma


def create_vectorstore(chunks, embedding_model):

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="vectorstore"
    )
    return vector_db