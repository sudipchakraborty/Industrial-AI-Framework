# app/agents/travel/travel_agent.py

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

class TravelAgent:

    def execute(
        self,
        query
    ):
        

        memory_result = (
    update_preference(
        query
    )
    )
        if memory_result:
            return memory_result




        query_lower = query.lower()

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

            print(plan)

            result = {}

            for step in plan.get(
                "steps",
                []
            ):

                tool_name = None

                # ---------------------------------
                # Handle JSON Plan
                # ---------------------------------

                if isinstance(
                    step,
                    dict
                ):

                    tool_name = (
                        step.get(
                            "tool"
                        )
                    )

                else:

                    tool_name = step

                # ---------------------------------
                # Flight Search
                # ---------------------------------

                if (
                    tool_name ==
                    "flight_search"
                ):

                    destination = (
                        step.get(
                            "destination",
                            "Delhi"
                        )
                        if isinstance(
                            step,
                            dict
                        )
                        else "Delhi"
                    )

                    result[
                        "flight"
                    ] = (
                        execute_step(
                            "flight_search",
                            search_flight,
                            destination
                        )
                    )

                # ---------------------------------
                # Hotel Search
                # ---------------------------------

                elif (
                    tool_name ==
                    "hotel_search"
                ):

                    location = (
                        step.get(
                            "location",
                            "Delhi"
                        )
                        if isinstance(
                            step,
                            dict
                        )
                        else "Delhi"
                    )

                    result[
                        "hotel"
                    ] = (
                        execute_step(
                            "hotel_search",
                            search_hotel,
                            location
                        )
                    )

                # ---------------------------------
                # Weather Search
                # ---------------------------------

                elif (
                    tool_name ==
                    "weather_search"
                ):

                    location = (
                        step.get(
                            "location",
                            "Delhi"
                        )
                        if isinstance(
                            step,
                            dict
                        )
                        else "Delhi"
                    )

                    result[
                        "weather"
                    ] = (
                        execute_step(
                            "weather_search",
                            get_weather,
                            location
                        )
                    )

            return result

        # =====================================
        # SINGLE TOOL EXECUTION
        # =====================================

        tool = llm_select_tool(
            query
        )

        print(
            "\nSelected Tool:"
        )

        print(tool)

        if (
            tool ==
            "flight_search"
        ):

            return execute_step(
                "flight_search",
                search_flight,
                "Delhi"
            )

        if (
            tool ==
            "hotel_search"
        ):

            return execute_step(
                "hotel_search",
                search_hotel,
                "Delhi"
            )

        if (
            tool ==
            "weather_search"
        ):

            return execute_step(
                "weather_search",
                get_weather,
                "Delhi"
            )

        return {
            "message":
            "No suitable travel tool found"
        }