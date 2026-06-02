from app.rag.retriever import retrieve
from app.llm.factory import get_llm

llm = get_llm()


def answer_question(query):

    docs = retrieve(query)

    context = "\n\n".join(docs)

    print("\nRetrieved Context:\n")
    print(context)

    prompt = f"""
You are an HR policy assistant.

Use ONLY the information from the context.

If relevant information exists in the context,
answer directly and concisely.

Only say
"I could not find that information in the uploaded policies."
when absolutely no relevant information exists.

Context:

{context}

Question:

{query}

Answer:
"""

    return llm.invoke(prompt)