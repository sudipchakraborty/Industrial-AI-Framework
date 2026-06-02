from app.rag.retriever import (
    retrieve
)

query = (
    "How many casual leaves are allowed?"
)

results = retrieve(
    query
)

print(
    "\nRetrieved Documents:\n"
)

for doc in results:

    print(
        "=" * 50
    )

    print(doc)