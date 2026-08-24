from agents.retriever import retrieve
from agents.generator import generate_answer
from agents.critic import critique_answer


query = input("Ask a question: ")

documents = retrieve(query)

answer = generate_answer(
    query,
    documents
)

print("\n" + "=" * 60)
print("GENERATED ANSWER")
print("=" * 60)

print(answer)


critique = critique_answer(
    query,
    answer,
    documents
)

print("\n" + "=" * 60)
print("CRITIC RESULT")
print("=" * 60)

print(critique)