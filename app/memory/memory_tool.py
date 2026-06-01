from app.memory.json_memory import (
    set_memory
)


def update_preference(
    query
):

    query = query.lower()

    if "prefer" in query:

        if "vistara" in query:

            set_memory(
                "preferred_airline",
                "Vistara"
            )

            return {
                "status":
                "saved",

                "preferred_airline":
                "Vistara"
            }

    return None