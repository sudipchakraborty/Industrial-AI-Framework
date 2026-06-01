from app.agents.travel.travel_agent import (
    TravelAgent
)

from app.agents.finance.finance_agent import (
    FinanceAgent
)

from app.agents.calendar.calendar_agent import (
    CalendarAgent
)

from app.agents.email.email_agent import (
    EmailAgent
)


COLLAB_AGENTS = {

    "travel":
        TravelAgent(),

    "finance":
        FinanceAgent(),

    "calendar":
        CalendarAgent(),

    "email":
        EmailAgent()
}