from copy import deepcopy

from app.agents.registry import AGENTS
from app.learning.learner import load_learning


def get_registry():

    agents = deepcopy(
        AGENTS
    )

    learned = load_learning()

    for agent_name, keywords in (
        learned.items()
    ):

        if agent_name in agents:

            existing = set(
                agents[agent_name][
                    "keywords"
                ]
            )

            for keyword in keywords:

                if keyword not in existing:

                    agents[
                        agent_name
                    ][
                        "keywords"
                    ].append(
                        keyword
                    )

    return agents