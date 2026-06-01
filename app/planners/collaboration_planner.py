def create_collaboration_plan(
    query
):

    query = query.lower()

    if (
        "business trip"
        in query
    ):

        return {

            "agents": [

                "travel",

                "finance",

                "calendar",

                "email"
            ]
        }

    return {

        "agents": [

            "travel"
        ]
    }