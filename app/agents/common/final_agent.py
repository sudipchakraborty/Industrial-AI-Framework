# final_agent.py

from langchain_core.messages import AIMessage

def final_agent(state):

    return {
        "messages": [
            AIMessage(
                content=f"""
Flights:
{state['flight_results']}

Hotels:
{state['hotel_results']}

Itinerary:
{state['itinerary']}
"""
            )
        ]
    }