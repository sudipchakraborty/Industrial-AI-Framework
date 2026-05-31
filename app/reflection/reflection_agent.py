import json

from app.llm.factory import get_llm

from app.reflection.reflection_prompt import (
    REFLECTION_PROMPT
)

llm = get_llm()


def validate_route(
    query,
    selected_agent
):

    prompt = (
        REFLECTION_PROMPT
        .replace(
            "{query}",
            query
        )
        .replace(
            "{agent}",
            selected_agent
        )
    )

    try:

        response = llm.invoke(
            prompt
        )

        print(
            "\nReflection Response:"
        )
        print(response)

        result = json.loads(
            response
        )

        return result

    except Exception as e:

        print(
            f"Reflection Error: {e}"
        )

        return {
            "valid": True,
            "suggested_agent":
                selected_agent,
            "confidence": 0.0
        }