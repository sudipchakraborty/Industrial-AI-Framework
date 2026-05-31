# app/routers/rule_router.py

import re

from langchain_community import agents
from app.agents.registry import AGENTS

from app.agents.registry_loader import (
    get_registry
)


def route(query):

    query = query.lower()

    best_agent = None
    best_score = 0

    agents = get_registry()
    for agent, info in agents.items():

        score = 0

        # Direct agent name match
        agent_pattern = r"\b" + re.escape(agent.lower()) + r"\b"

        if re.search(agent_pattern, query):
            score += 5

        # Keyword matching
        for keyword in info["keywords"]:

            keyword_pattern = (
                r"\b"
                + re.escape(keyword.lower())
                + r"\b"
            )

            if re.search(keyword_pattern, query):
                score += 1

        if score > best_score:
            best_score = score
            best_agent = agent

    # Confidence calculation
    if best_score >= 3:
        confidence = 0.95

    elif best_score == 2:
        confidence = 0.80

    elif best_score == 1:
        confidence = 0.70

    else:
        confidence = 0.0

    return {
        "agent": best_agent,
        "score": best_score,
        "confidence": confidence
    }