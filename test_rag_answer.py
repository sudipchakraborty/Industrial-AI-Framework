from app.rag.rag_pipeline import (
    answer_question
)

response = answer_question(
    "How many casual leaves are allowed?"
)

print(
    "\nAnswer:\n"
)

print(
    response
)