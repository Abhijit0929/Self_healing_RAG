from agents.retriever import retrieve


query = input("Enter query: ")

documents = retrieve(query)

print("\n" + "=" * 70)
print("RETRIEVED DOCUMENTS")
print("=" * 70)

for i, doc in enumerate(documents, 1):

    print(f"\n--- CHUNK {i} ---")

    print("Metadata:")
    print(doc.metadata)

    print("\nContent:")
    print(doc.page_content)

    print("\n" + "-" * 70)