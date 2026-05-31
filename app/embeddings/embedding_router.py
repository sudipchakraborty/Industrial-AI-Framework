from sentence_transformers import util

from app.embeddings.embedder import get_embedding
from app.embeddings.vector_store import AGENT_EMBEDDINGS

def embedding_route(query):

    query_embedding = get_embedding(query)

    scores = {}

    best_agent = None
    best_score = -1

    for agent, embedding in AGENT_EMBEDDINGS.items():

        score = util.cos_sim(
            query_embedding,
            embedding
        ).item()

        scores[agent] = round(score, 3)

        if score > best_score:
            best_score = score
            best_agent = agent

    return {
        "agent": best_agent,
        "confidence": round(best_score, 3),
        "scores": scores
    }