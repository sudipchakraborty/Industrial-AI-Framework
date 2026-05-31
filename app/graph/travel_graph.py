from langgraph.graph import StateGraph
from langgraph.graph import START, END

from app.state.travel_state import TravelState

from app.agents.supervisor_agent import supervisor_agent
from app.agents.general_agent import general_agent

from app.agents.flight_agent import flight_agent
from app.agents.hotel_agent import hotel_agent
from app.agents.itinerary_agent import itinerary_agent

from app.graph.router import route_after_supervisor

from app.database.postgres import get_checkpointer


def create_graph():

    graph = StateGraph(TravelState)

    graph.add_node(
        "supervisor_agent",
        supervisor_agent
    )

    graph.add_node(
        "general_agent",
        general_agent
    )

    graph.add_node(
        "flight_agent",
        flight_agent
    )

    graph.add_node(
        "hotel_agent",
        hotel_agent
    )

    graph.add_node(
        "itinerary_agent",
        itinerary_agent
    )

    graph.add_edge(
        START,
        "supervisor_agent"
    )

    graph.add_conditional_edges(
        "supervisor_agent",
        route_after_supervisor,
        {
            "general_agent": "general_agent",
            "flight_agent": "flight_agent",
            "hotel_agent": "hotel_agent",
            "itinerary_agent": "itinerary_agent"
        }
    )

    graph.add_edge(
        "general_agent",
        END
    )

    graph.add_edge(
        "flight_agent",
        END
    )

    graph.add_edge(
        "hotel_agent",
        END
    )

    graph.add_edge(
        "itinerary_agent",
        END
    )

    return graph.compile(
        checkpointer=get_checkpointer()
    )