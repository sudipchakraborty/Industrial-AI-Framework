from app.planners.collaboration_planner import (
    create_collaboration_plan
)

from app.agents.collaboration_registry import (
    COLLAB_AGENTS
)


def execute_collaboration(
    query
):

    plan = (
        create_collaboration_plan(
            query
        )
    )

    print(
        "\nCollaboration Plan:"
    )

    print(plan)

    results = {}

    for agent_name in (
        plan["agents"]
    ):

        agent = (
            COLLAB_AGENTS[
                agent_name
            ]
        )

        results[
            agent_name
        ] = (
            agent.execute(
                query
            )
        )

    return results