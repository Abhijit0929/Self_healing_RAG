from config import llm


def generate_answer(question, documents):

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:
"I don't have enough information."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content