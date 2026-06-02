# app/reflection/reflection_agent.py

import json
import re

from app.llm.factory import get_llm

from app.reflection.reflection_prompt import (
    REFLECTION_PROMPT
)

llm = get_llm()

REFLECTION_OVERRIDE_THRESHOLD = 0.95


def _extract_json(response):

    if not response:

        raise ValueError(
            "Empty reflection response"
        )

    # ----------------------------------
    # Direct JSON
    # ----------------------------------

    try:

        return json.loads(
            response
        )

    except Exception:

        pass

    # ----------------------------------
    # Extract JSON block
    # ----------------------------------

    match = re.search(
        r"\{.*\}",
        response,
        re.DOTALL
    )

    if not match:

        raise ValueError(
            "No JSON found in response"
        )

    json_text = match.group(
        0
    )

    return json.loads(
        json_text
    )


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

        print(
            response
        )

        result = _extract_json(
            response
        )

        # --------------------------
        # Safety defaults
        # --------------------------

        result.setdefault(
            "valid",
            True
        )

        result.setdefault(
            "suggested_agent",
            selected_agent
        )

        result.setdefault(
            "confidence",
            0.0
        )

        # --------------------------
        # Normalize confidence
        # --------------------------

        try:

            result[
                "confidence"
            ] = float(
                result[
                    "confidence"
                ]
            )

        except Exception:

            result[
                "confidence"
            ] = 0.0

        # --------------------------
        # Prevent weak overrides
        # --------------------------

        if (

            result[
                "valid"
            ] is False

            and

            result[
                "confidence"
            ]
            < REFLECTION_OVERRIDE_THRESHOLD

        ):

            print(
                "\nReflection override rejected"
            )

            print(
                f"Confidence: "
                f"{result['confidence']}"
            )

            return {

                "valid":
                    True,

                "suggested_agent":
                    selected_agent,

                "confidence":
                    result[
                        "confidence"
                    ]
            }

        return result

    except Exception as e:

        print(
            f"Reflection Error: {e}"
        )

        return {

            "valid":
                True,

            "suggested_agent":
                selected_agent,

            "confidence":
                0.0
        }