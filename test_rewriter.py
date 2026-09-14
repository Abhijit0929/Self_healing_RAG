from agents.rewriter import rewrite_query

question = "what alogrithm were used for customer churn prediciton?"

answer = "I dont have enough information."

critique="""
VERDICT: INVALID
SCORE:0.20
REASON: The retrieved context discusses customer customer churn but does not contain the specific  
alogrithms used in the study
"""

rewritten_query= rewrite_query(
    question,
    answer,
    critique
)

print("\n"+"="*60)
print("ORIGINAL QUESTION")
print("="*60)
print(question)

print("\n"+"="*60)
print("REWRITTEN QUESTION")
print("="*60)
print(rewritten_query)  

print("\n"+"="*60)
print("REWRITER TEST COMPLETED")
print("="*60)