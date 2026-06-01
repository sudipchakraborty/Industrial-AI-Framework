# app/agents/email/email_agent.py

from app.observability.metrics import (
    increment
)


class EmailAgent:

    def execute(
        self,
        query
    ):

        increment(
            "email_agent_calls"
        )

        return {

            "status":
                "drafted"
        }