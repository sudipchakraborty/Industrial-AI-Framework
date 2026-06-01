# app/agents/finance/finance_agent.py

from app.observability.metrics import (
    increment
)


class FinanceAgent:

    def execute(
        self,
        query
    ):

        increment(
            "finance_agent_calls"
        )

        return {

            "approved":
                True,

            "budget":
                25000
        }