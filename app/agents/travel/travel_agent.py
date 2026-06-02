from app.planners.planner_agent import (
    create_plan
)

from app.tools.tool_selector import (
    llm_select_tool
)

from app.tools.flight_tool import (
    search_flight
)

from app.tools.hotel_tool import (
    search_hotel
)

from app.tools.weather_tool import (
    get_weather
)

from app.executors.plan_executor import (
    execute_step
)

from app.memory.memory_tool import (
    update_preference
)

from app.observability.metrics import (
    increment
)


class TravelAgent:

    def execute(
        self,
        query
    ):

        # =====================================
        # METRICS
        # =====================================

        increment(
            "travel_agent_calls"
        )

        # =====================================
        # MEMORY UPDATE
        # =====================================

        memory_result = (
            update_preference(
                query
            )
        )

        if memory_result:

            return memory_result

        query_lower = (
            query.lower()
        )

        # =====================================
        # MULTI-STEP PLANNING
        # =====================================

        if "plan" in query_lower:

            plan = create_plan(
                query
            )

            print(
                "\nGenerated Plan:"
            )

            print(
                plan
            )

            result = {}

            for step in plan.get(
                "steps",
                []
            ):

                if isinstance(
                    step,
                    dict
                ):

                    tool_name = (
                        step.get("tool")
                        or
                        step.get("type")
                    )

                else:

                    tool_name = step

                # -----------------------------
                # Flight
                # -----------------------------

                if (
                    tool_name
                    ==
                    "flight_search"
                ):

                    result[
                        "flight"
                    ] = execute_step(
                        "flight_search",
                        search_flight,
                        "Delhi"
                    )

                # -----------------------------
                # Hotel
                # -----------------------------

                elif (
                    tool_name
                    ==
                    "hotel_search"
                ):

                    result[
                        "hotel"
                    ] = execute_step(
                        "hotel_search",
                        search_hotel,
                        "Delhi"
                    )

                # -----------------------------
                # Weather
                # -----------------------------

                elif (
                    tool_name
                    ==
                    "weather_search"
                ):

                    result[
                        "weather"
                    ] = execute_step(
                        "weather_search",
                        get_weather,
                        "Delhi"
                    )

            return result

        # =====================================
        # PHASE-13 FAST TOOL ROUTER
        # =====================================

        tool = llm_select_tool(
            query
        )

        print(
            "\nSelected Tool:"
        )

        print(
            tool
        )

        # =====================================
        # EXECUTE TOOL
        # =====================================

        if (
            tool
            ==
            "flight_search"
        ):

            return execute_step(
                "flight_search",
                search_flight,
                "Delhi"
            )

        if (
            tool
            ==
            "hotel_search"
        ):

            return execute_step(
                "hotel_search",
                search_hotel,
                "Delhi"
            )

        if (
            tool
            ==
            "weather_search"
        ):

            return execute_step(
                "weather_search",
                get_weather,
                "Delhi"
            )

        # =====================================
        # FALLBACK
        # =====================================

        return {

            "message":
                "No suitable travel tool found",

            "query":
                query
        }
