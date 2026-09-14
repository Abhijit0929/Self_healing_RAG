from config import llm 

def rewrite_query(question,answer,critique):

    prompt = f"""
Your are a query-rewriting agent in a self-healing,RAG system.

The system attempted to answer a question,but the critic determined 
that the answer was not sufficently grounded in the retrieved context.


Your job is to rewrite the user's original question into a better 
search query that will help the retrieval system to find the missing information.


original Question:
{question}

perivous answer:
{answer}

critique Feedback:
{critique}

Rules:

1. Preserve the Original intent of the question.
2. Make the query more specific.
3. Include important conpcepts fromt the critic feedback.
4. Do not answer the question.
5. Return ONLY the rewritten search query.

Rewritten Query:
"""

    response = llm.invoke(prompt)
    return response.content.strip()