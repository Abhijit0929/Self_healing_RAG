from agents.retriever import retrieve
from agents.generator import generate_answer
from agents.critic import critique_answer
from agents.rewriter import rewrite_query


MAX_RETRIES = 2


def self_healing_rag(question):
    """
    Runs the complete self-healing RAG workflow.

    Flow:
    Question → Retrieve → Generate → Critic
                         ↓
                    Valid answer?
                    ↓         ↓
                   Yes        No
                    ↓         ↓
                Final answer  Rewrite query
                                  ↓
                              Retry retrieval
    """

    current_query = question

    for attempt in range(MAX_RETRIES + 1):

        print("\n" + "=" * 60)
        print(f"ATTEMPT {attempt + 1}")
        print("=" * 60)

        print(f"\n🔎 Search Query:\n{current_query}")

        # Step 1: Retrieve relevant documents
        documents = retrieve(current_query)

        print(f"\n📄 Documents Retrieved: {len(documents)}")

        # Step 2: Generate an answer
        answer = generate_answer(
            current_query,
            documents
        )

        print(f"\n🤖 Generated Answer:\n{answer}")

        # Step 3: Critique the generated answer
        critique = critique_answer(
            current_query,
            answer,
            documents
        )

        print(f"\n🧐 Critic Feedback:\n{critique}")

        # Step 4: Check whether the answer is valid
        if "VERDICT: VALID" in critique.upper():

            print("\n✅ Answer accepted by critic.")

            return answer

        # Step 5: If invalid, rewrite the query
        if attempt < MAX_RETRIES:

            print("\n⚠️ Answer rejected. Rewriting query...")

            current_query = rewrite_query(
                question,
                answer,
                critique
            )

            print(f"\n✍️ Rewritten Query:\n{current_query}")

        else:

            print("\n❌ Maximum retries reached.")

            return answer


if __name__ == "__main__":

    print("=" * 60)
    print("🧠 SELF-HEALING RAG SYSTEM")
    print("=" * 60)

    question = input("\n🧑 Enter your question: ")

    final_answer = self_healing_rag(question)

    print("\n" + "=" * 60)
    print("🎯 FINAL ANSWER")
    print("=" * 60)
    print(final_answer)