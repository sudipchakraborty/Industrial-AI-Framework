from langchain_core.messages import AIMessage

def supervisor_agent(state):

    query = state["user_query"].lower()

    if any(word in query for word in [
        "flight",
        "airline",
        "airport",
        "ticket"
    ]):
        next_agent = "flight_agent"

    elif any(word in query for word in [
        "hotel",
        "stay",
        "resort"
    ]):
        next_agent = "hotel_agent"

    elif any(word in query for word in [
        "travel",
        "trip",
        "vacation"
    ]):
        next_agent = "itinerary_agent"

    else:
        next_agent = "general_agent"

    return {
        "next_agent": next_agent,
        "messages": [
            AIMessage(
                content=f"Supervisor selected {next_agent}"
            )
        ]
    }