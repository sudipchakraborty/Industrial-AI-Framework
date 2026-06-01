# app/routers/supervisor.py

from app.routers.rule_router import route
from app.routers.llm_router import llm_route

from app.embeddings.embedding_router import (
    embedding_route
)

from app.routers.agent_loader import (
    AGENT_OBJECTS
)

from app.utils.logger import (
    log_route
)

from app.reflection.reflection_agent import (
    validate_route
)

from app.observability.metrics import (
    increment
)

from app.learning.learner import (
    learn
)

from app.executors.collaboration_executor import (
    execute_collaboration
)


RULE_THRESHOLD = 0.70
EMBEDDING_THRESHOLD = 0.30
LLM_THRESHOLD = 0.70


def execute_with_reflection(
    query,
    agent_name
):
    """
    Final validation before executing an agent.
    """

    reflection = validate_route(
        query,
        agent_name
    )

    print("\nReflection:")
    print(reflection)

    log_route(
        query,
        "reflection_agent",
        reflection
    )

    # Reflection correction
    if reflection.get("valid") is False:

        increment(
            "reflection_corrections"
        )

        agent_name = reflection.get(
            "suggested_agent",
            agent_name
        )

        print(
            f"\nReflection corrected route -> {agent_name}"
        )

    # Agent metrics
    metric_name = (
        f"{agent_name}_agent_calls"
    )

    increment(
        metric_name
    )

    # Self-learning
    learn(
        query,
        agent_name
    )

    # Execute final agent
    agent = AGENT_OBJECTS[
        agent_name
    ]

    return agent.execute(
        query
    )


def supervisor(query):

    # =====================================
    # MULTI-AGENT COLLABORATION
    # =====================================

    if (
        "business trip"
        in query.lower()
    ):

        print(
            "\nCollaboration Workflow Triggered"
        )

        return execute_collaboration(
            query
        )

    # ==================================================
    # STEP 1 : RULE ROUTER
    # ==================================================

    rule_result = route(query)

    print("\nRule Router:")
    print(rule_result)

    log_route(
        query,
        "rule_router",
        rule_result
    )

    if (
        rule_result.get("agent") is not None
        and
        rule_result.get("confidence", 0)
        >= RULE_THRESHOLD
    ):

        increment(
            "rule_router_hits"
        )

        return execute_with_reflection(
            query,
            rule_result["agent"]
        )

    # ==================================================
    # STEP 2 : EMBEDDING ROUTER
    # ==================================================

    embedding_result = embedding_route(
        query
    )

    print("\nEmbedding Router:")
    print(embedding_result)

    log_route(
        query,
        "embedding_router",
        embedding_result
    )

    if (
        embedding_result.get("agent") is not None
        and
        embedding_result.get("confidence", 0)
        >= EMBEDDING_THRESHOLD
    ):

        increment(
            "embedding_router_hits"
        )

        return execute_with_reflection(
            query,
            embedding_result["agent"]
        )

    # ==================================================
    # STEP 3 : LLM ROUTER
    # ==================================================

    increment(
        "llm_router_hits"
    )

    llm_result = llm_route(
        query
    )

    print("\nLLM Router:")
    print(llm_result)

    log_route(
        query,
        "llm_router",
        llm_result
    )

    if (
        llm_result.get("agent") is None
        or
        llm_result.get("confidence", 0)
        < LLM_THRESHOLD
    ):

        return (
            "\nI am not sure.\n"
            "Please select:\n\n"
            "1. Home\n"
            "2. Office\n"
            "3. Doctor\n"
            "4. Travel\n"
            "5. General\n"
        )

    return execute_with_reflection(
        query,
        llm_result["agent"]
    )