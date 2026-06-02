from app.approval.approval_agent import (
    request_approval
)

from app.agents.collaboration_registry import (
    COLLAB_AGENTS
)

from app.executors.multi_agent_detector import (
    detect_agents
)


def execute_collaboration(
    query
):

    # =====================================
    # FAST PHASE-13 COLLABORATION
    # =====================================

    agents = detect_agents(
        query
    )

    plan = {

        "agents": agents

    }

    print(
        "\nCollaboration Plan:"
    )

    print(
        plan
    )

    if not request_approval(
        plan
    ):

        print(
            "\nCollaboration denied."
        )

        return {}

    results = {}

    for agent_name in agents:

        if (
            agent_name
            not in COLLAB_AGENTS
        ):

            continue

        agent = (
            COLLAB_AGENTS[
                agent_name
            ]
        )

        try:

            results[
                agent_name
            ] = (
                agent.execute(
                    query
                )
            )

        except Exception as e:

            results[
                agent_name
            ] = {

                "error":
                    str(e)

            }

    return results