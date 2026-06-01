# app/tools/tool_router.py

def select_tool(query):

    query = query.lower()

    if any(
        word in query
        for word in [
            "flight",
            "airline",
            "airport",
            "ticket"
        ]
    ):
        return "flight_search"

    if any(
        word in query
        for word in [
            "hotel",
            "accommodation",
            "room"
        ]
    ):
        return "hotel_search"

    if any(
        word in query
        for word in [
            "weather",
            "rain",
            "temperature"
        ]
    ):
        return "weather_search"

    return None