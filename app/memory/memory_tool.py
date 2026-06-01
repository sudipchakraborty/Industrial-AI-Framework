# app/memory/memory_tool.py

from app.memory.json_memory import (
    set_memory
)


def update_preference(
    query
):

    query_lower = (
        query.lower()
    )

    # -------------------------
    # Airlines
    # -------------------------

    airlines = [

        "vistara",
        "emirates",
        "indigo",
        "air india",
        "spicejet",
        "akasa"
    ]

    for airline in airlines:

        if (
            "prefer" in query_lower
            and
            airline in query_lower
        ):

            set_memory(
                "preferred_airline",
                airline.title()
            )

            return {

                "status":
                "saved",

                "preferred_airline":
                airline.title()
            }

    # -------------------------
    # Hotels
    # -------------------------

    hotels = [

        "taj",
        "marriott",
        "hyatt",
        "hilton"
    ]

    for hotel in hotels:

        if (
            "prefer" in query_lower
            and
            hotel in query_lower
        ):

            set_memory(
                "preferred_hotel",
                hotel.title()
            )

            return {

                "status":
                "saved",

                "preferred_hotel":
                hotel.title()
            }

    # -------------------------
    # Seat Preference
    # -------------------------

    if (
        "window seat"
        in query_lower
    ):

        set_memory(
            "seat_preference",
            "Window"
        )

        return {

            "status":
            "saved",

            "seat_preference":
            "Window"
        }

    if (
        "aisle seat"
        in query_lower
    ):

        set_memory(
            "seat_preference",
            "Aisle"
        )

        return {

            "status":
            "saved",

            "seat_preference":
            "Aisle"
        }

    return None