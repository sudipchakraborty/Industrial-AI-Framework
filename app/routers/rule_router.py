# app/routers/rule_router.py

import re

from app.agents.registry_loader import (
    get_registry
)


# ----------------------------------
# HR keywords deserve higher weight
# ----------------------------------

HIGH_PRIORITY_KEYWORDS = {

    # Existing HR keywords

    "leave",
    "leaves",
    "casual",
    "casual leave",
    "casual leaves",
    "sick leave",
    "earned leave",
    "marriage leave",
    "marriage",
    "bereavement leave",
    "probation",
    "policy",
    "reimbursement",
    "travel reimbursement",
    "employee handbook",
    "leave policy",
    "hr policy",

    # Attendance keywords

    "attendance",
    "absent",
    "present",
    "checked in",
    "late employee",
    "late employees",
    "employee attendance"
}


def route(query):

    query = query.lower()

    best_agent = None
    best_score = 0

    agents = get_registry()

    for agent, info in agents.items():

        score = 0

        # --------------------------
        # Direct Agent Name Match
        # --------------------------

        agent_pattern = (
            r"\b"
            + re.escape(
                agent.lower()
            )
            + r"\b"
        )

        if re.search(
            agent_pattern,
            query
        ):
            score += 5

        # --------------------------
        # Keyword Matching
        # --------------------------

        for keyword in info["keywords"]:

            keyword_pattern = (
                r"\b"
                + re.escape(
                    keyword.lower()
                )
                + r"\b"
            )

            if re.search(
                keyword_pattern,
                query
            ):

                # --------------------------------
                # HR-related phrases get priority
                # --------------------------------

                if keyword.lower() in HIGH_PRIORITY_KEYWORDS:

                    score += 3

                else:

                    score += 1

        if score > best_score:

            best_score = score
            best_agent = agent

    # --------------------------
    # Confidence
    # --------------------------

    if best_score >= 5:

        confidence = 0.99

    elif best_score >= 3:

        confidence = 0.90

    elif best_score >= 2:

        confidence = 0.75

    else:

        confidence = 0.0

    return {

        "agent":
            best_agent,

        "score":
            best_score,

        "confidence":
            confidence
}