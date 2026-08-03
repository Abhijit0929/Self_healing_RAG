from agents.retriever import retrieve
from agents.generator import generate_answer

print("=" * 60)
print("🤖 Self-Healing RAG")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    query = input("\n🧑 You: ")

    if query.lower() in ["exit", "quit", "q"]:
        print("\n👋 Goodbye!")
        break

    documents = retrieve(query)

    answer = generate_answer(query, documents)

    print(f"\n🤖 Assistant:\n{answer}")