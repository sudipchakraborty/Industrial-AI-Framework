# app/executors/multi_agent_detector.py

def detect_agents(query):

    query = query.lower()

    agents = []

    # =====================================
    # TRAVEL
    # =====================================

    if any(
        word in query
        for word in [
            "travel",
            "trip",
            "flight",
            "hotel",
            "airport"
        ]
    ):

        agents.append(
            "travel"
        )

    # =====================================
    # DOCTOR
    # =====================================

    if any(
        word in query
        for word in [
            "doctor",
            "health",
            "checkup",
            "hospital",
            "medicine"
        ]
    ):

        agents.append(
            "doctor"
        )

    # =====================================
    # OFFICE
    # =====================================

    if any(
        word in query
        for word in [
            "office",
            "meeting",
            "manager",
            "leave",
            "project"
        ]
    ):

        agents.append(
            "office"
        )

    return list(
        set(agents)
    )