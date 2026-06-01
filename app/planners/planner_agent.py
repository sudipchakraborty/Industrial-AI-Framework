import json
import re

from app.llm.factory import (
    get_llm
)

from app.planners.planner_prompt import (
    PLANNER_PROMPT
)

from app.observability.metrics import (
    increment
)


llm = get_llm()


def clean_json(
    json_text
):

    json_text = re.sub(
        r"//.*",
        "",
        json_text
    )

    return json_text


def create_plan(
    query
):

    increment(
        "planner_calls"
    )

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

    print(
        response
    )

    # =====================================
    # Try direct JSON parse
    # =====================================

    try:

        return json.loads(
            response
        )

    except Exception:

        pass

    # =====================================
    # Extract JSON block
    # =====================================

    try:

        match = re.search(
            r"\{.*\}",
            response,
            re.DOTALL
        )

        if match:

            json_text = (
                match.group(0)
            )

            json_text = clean_json(
                json_text
            )

            return json.loads(
                json_text
            )

    except Exception as e:

        print(
            "\nPlanner Parse Error:"
        )

        print(
            e
        )

    return {

        "steps": []
    }