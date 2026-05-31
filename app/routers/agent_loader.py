from app.agents.home.home_agent import HomeAgent
from app.agents.office.office_agent import OfficeAgent
from app.agents.doctor.doctor_agent import DoctorAgent
from app.agents.travel.travel_agent import TravelAgent
from app.agents.general.general_agent import (
    GeneralAgent
)

AGENT_OBJECTS = {

    "home": HomeAgent(),

    "office": OfficeAgent(),

    "doctor": DoctorAgent(),

    "travel": TravelAgent(),

    "general": GeneralAgent()
}