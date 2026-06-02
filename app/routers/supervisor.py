# app/routers/supervisor.py

from app import agents
from app.routers.rule_router import route

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

from app.executors.multi_agent_detector import (
    detect_agents
)

# ==========================================
# PHASE-10 MULTI-LLM VOTING ROUTER
# ==========================================

try:

    from app.voting.voting_router import (
        VotingRouter
    )

    from app.providers.openai_provider import (
        OpenAIProvider
    )

    from app.providers.gemini_provider import (
        GeminiProvider
    )

    from app.providers.groq_provider import (
        GroqProvider
    )

    from app.providers.ollama_provider import (
        OllamaProvider
    )

    VOTING_ENABLED = True

except Exception as e:

    print(
        f"\nVoting Router disabled: {e}"
    )

    VOTING_ENABLED = False


# ==========================================
# THRESHOLDS
# ==========================================

RULE_THRESHOLD = 0.85

EMBEDDING_THRESHOLD = 0.25

VOTING_THRESHOLD = 0.55

REFLECTION_OVERRIDE_THRESHOLD = 0.95

# ==========================================
# PHASE-12 FAST CONSENSUS
# ==========================================

FAST_RULE_THRESHOLD = 0.90

FAST_EMBEDDING_THRESHOLD = 0.40


# ==========================================
# CREATE VOTING ROUTER
# ==========================================

if VOTING_ENABLED:

    try:

        voting_router = VotingRouter(
            OpenAIProvider(),
            GeminiProvider(),
            GroqProvider(),
            OllamaProvider()
        )

    except Exception as e:

        print(
            f"\nVoting Router init failed: {e}"
        )

        VOTING_ENABLED = False


# ==========================================
# FAST EXECUTION
# ==========================================

def execute_agent_only(
    query,
    agent_name
):

    metric_name = (
        f"{agent_name}_agent_calls"
    )

    increment(
        metric_name
    )

    learn(
        query,
        agent_name
    )

    if agent_name not in AGENT_OBJECTS:

        return (
            f"\nAgent not found: "
            f"{agent_name}"
        )

    agent = AGENT_OBJECTS[
        agent_name
    ]

    return agent.execute(
        query
    )


# ==========================================
# REFLECTION EXECUTION
# ==========================================

def execute_with_reflection(
    query,
    agent_name
):

    reflection = validate_route(
        query,
        agent_name
    )

    print(
        "\nReflection:"
    )

    print(
        reflection
    )

    log_route(
        query,
        "reflection_agent",
        reflection
    )

    if (

        reflection.get("valid")
        is False

        and

        reflection.get(
            "confidence",
            0
        )
        >= REFLECTION_OVERRIDE_THRESHOLD

    ):

        increment(
            "reflection_corrections"
        )

        agent_name = reflection.get(
            "suggested_agent",
            agent_name
        )

        print(
            f"\nReflection corrected route -> "
            f"{agent_name}"
        )

    elif (

        reflection.get("valid")
        is False

    ):

        print(
            "\nReflection suggested a correction "
            "but confidence was below threshold."
        )

        print(
            f"Reflection Confidence: "
            f"{reflection.get('confidence', 0)}"
        )

        print(
            f"Keeping original agent: "
            f"{agent_name}"
        )

    metric_name = (
        f"{agent_name}_agent_calls"
    )

    increment(
        metric_name
    )

    learn(
        query,
        agent_name
    )

    if agent_name not in AGENT_OBJECTS:

        return (
            f"\nAgent not found: "
            f"{agent_name}"
        )

    agent = AGENT_OBJECTS[
        agent_name
    ]

    return agent.execute(
        query
    )


# ==========================================
# SUPERVISOR
# ==========================================

def supervisor(query):

    from app.executors.multi_agent_detector import (
    detect_agents
)

    agents = detect_agents(
        query
    )

    if len(agents) > 1:

        print(
            "\nMULTI AGENT DETECTED"
        )

        return execute_collaboration(
            query
        )


      # =====================================
    # PHASE-13 MULTI AGENT DETECTION
    # =====================================

    detected_agents = detect_agents(
        query
    )

    if len(
        detected_agents
    ) > 1:

        print(
            "\nMULTI AGENT DETECTED:"
        )

        print(
            detected_agents
        )

        return execute_collaboration(
            query
        )


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

    # =====================================
    # STEP 1 : RULE ROUTER
    # =====================================

    rule_result = route(
        query
    )

    print(
        "\nRule Router:"
    )

    print(
        rule_result
    )

    log_route(
        query,
        "rule_router",
        rule_result
    )

    if (

        rule_result.get(
            "agent"
        )
        is not None

    ):

        confidence = rule_result.get(
            "confidence",
            0
        )

        # =====================================
        # PHASE-12 FAST CONSENSUS MODE
        # =====================================

        if confidence >= FAST_RULE_THRESHOLD:

            print(
                "\nFAST CONSENSUS MODE"
            )

            increment(
                "fast_path_hits"
            )

            return execute_agent_only(
                query,
                rule_result[
                    "agent"
                ]
            )

        # =====================================
        # NORMAL RULE ROUTER
        # =====================================

        if confidence >= RULE_THRESHOLD:

            increment(
                "rule_router_hits"
            )

            return execute_with_reflection(
                query,
                rule_result[
                    "agent"
                ]
            )

    # =====================================
    # STEP 2 : EMBEDDING ROUTER
    # =====================================

    embedding_result = (
        embedding_route(
            query
        )
    )

    print(
        "\nEmbedding Router:"
    )

    print(
        embedding_result
    )

    log_route(
        query,
        "embedding_router",
        embedding_result
    )

    if (

        embedding_result.get(
            "agent"
        )
        is not None

    ):

        confidence = embedding_result.get(
            "confidence",
            0
        )

        # =====================================
        # PHASE-12 FAST EMBEDDING MODE
        # =====================================

        if confidence >= FAST_EMBEDDING_THRESHOLD:

            print(
                "\nFAST EMBEDDING MODE"
            )

            increment(
                "fast_path_hits"
            )

            return execute_agent_only(
                query,
                embedding_result[
                    "agent"
                ]
            )

        # =====================================
        # NORMAL EMBEDDING PATH
        # =====================================

        if confidence >= EMBEDDING_THRESHOLD:

            increment(
                "embedding_router_hits"
            )

            return execute_with_reflection(
                query,
                embedding_result[
                    "agent"
                ]
            )

    # =====================================
    # STEP 3 : VOTING ROUTER
    # =====================================

    if VOTING_ENABLED:

        increment(
            "voting_router_hits"
        )

        vote_result = (
            voting_router.route(
                query
            )
        )

        print(
            "\nVoting Router Results"
        )

        for vote in vote_result.get(
            "votes",
            []
        ):

            print(
                f"{vote.provider}"
                f" -> "
                f"{vote.agent}"
                f" "
                f"({vote.confidence})"
            )

        print(
            "\nConsensus:"
        )

        print(
            vote_result.get(
                "selected_agent"
            )
        )

        print(
            "\nConsensus Confidence:"
        )

        print(
            vote_result.get(
                "confidence"
            )
        )

        log_route(
            query,
            "voting_router",
            vote_result
        )

        if (

            vote_result.get(
                "confidence",
                0
            )
            < VOTING_THRESHOLD

        ):

            return (
                "\nVoting confidence too low.\n"
                "Human approval required."
            )

        return execute_with_reflection(
            query,
            vote_result[
                "selected_agent"
            ]
        )

    # =====================================
    # FALLBACK
    # =====================================

    return (
        "\nUnable to determine intent.\n"
        "Please choose:\n\n"
        "1. Home\n"
        "2. Office\n"
        "3. Doctor\n"
        "4. Travel\n"
        "5. General\n"
    )