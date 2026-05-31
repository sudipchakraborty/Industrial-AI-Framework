# itinerary_agent.py

from langchain_core.messages import AIMessage

def itinerary_agent(state):

    return {
        "itinerary": "Sample Itinerary",
        "messages": [
            AIMessage(content="Itinerary Agent Executed")
        ]
    }