from app.rag.embedder import (
    model
)

from app.rag.vector_store import (
    collection
)


def retrieve(query):

    query_embedding = model.encode(
        [query]
    )

    results = collection.query(

        query_embeddings=
        query_embedding.tolist(),

        n_results=3

    )

    return results["documents"][0]