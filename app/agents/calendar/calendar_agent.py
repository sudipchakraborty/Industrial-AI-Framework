# app/agents/calendar/calendar_agent.py

from app.observability.metrics import (
    increment
)


class CalendarAgent:

    def execute(
        self,
        query
    ):

        increment(
            "calendar_agent_calls"
        )

        return {

            "available":
                True
        }