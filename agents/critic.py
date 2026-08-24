from config import llm


def critique_answer(question, answer, documents):

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    prompt = f"""
You are a strict factuality critic for a Retrieval-Augmented Generation system.

Your job is to determine whether the generated answer is fully supported
by the retrieved context.

Do NOT use your own knowledge.

QUESTION:
{question}

RETRIEVED CONTEXT:
{context}

GENERATED ANSWER:
{answer}

Evaluate the answer.

Return ONLY the following format:

VERDICT: VALID
SCORE: 0.95
REASON: The answer is fully supported by the retrieved context.

OR:

VERDICT: INVALID
SCORE: 0.30
REASON: The answer contains information that is not supported by the retrieved context.

Rules:
- VALID means the answer is supported by the retrieved context.
- INVALID means the answer contains unsupported, contradictory, or hallucinated information.
- SCORE must be between 0 and 1.
- Do not add information from your own knowledge.
"""

    response = llm.invoke(prompt)

    return response.content