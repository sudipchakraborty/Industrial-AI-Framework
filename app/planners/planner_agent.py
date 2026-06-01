import json
import re

from app.llm.factory import get_llm

from app.planners.planner_prompt import (
    PLANNER_PROMPT
)

llm = get_llm()


def create_plan(query):

    prompt = (
        PLANNER_PROMPT
        .replace(
            "{query}",
            query
        )
    )

    response = llm.invoke(
        prompt
    )

    print(
        "\nPlanner Response:"
    )

    print(response)

    try:

        return json.loads(
            response
        )

    except:

        pass

    # =====================================
    # Extract JSON Block
    # =====================================

    try:

        match = re.search(
            r'\{.*\}',
            response,
            re.DOTALL
        )

        if match:

            json_text = (
                match.group(0)
            )

            return json.loads(
                json_text
            )

    except Exception as e:

        print(
            f"Planner Parse Error: {e}"
        )

    return {
        "steps": []
    }