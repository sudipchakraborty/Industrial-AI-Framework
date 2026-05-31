# app/routers/llm_router.py

import json

from app.llm.factory import get_llm

from app.llm.router_prompt import (
    ROUTER_PROMPT
)

VALID_AGENTS = [
    "home",
    "office",
    "doctor",
    "travel",
    "general"
]

llm = get_llm()


def llm_route(query):

    prompt = (
        ROUTER_PROMPT
        + "\n\nUser Query:\n"
        + query
    )

    try:

        response = llm.invoke(prompt)

        # Debug (optional)
        print("\nRaw LLM Response:")
        print(response)

        result = json.loads(response)

        agent = result.get("agent")
        confidence = float(
            result.get(
                "confidence",
                0.0
            )
        )

        # Validate agent name
        if agent not in VALID_AGENTS:

            return {
                "agent": "general",
                "confidence": 0.50
            }

        return {
            "agent": agent,
            "confidence": confidence
        }

    except json.JSONDecodeError:

        print(
            "\nLLM returned invalid JSON."
        )

        return {
            "agent": "general",
            "confidence": 0.0
        }

    except Exception as e:

        print(
            f"\nLLM Router Error: {e}"
        )

        return {
            "agent": "general",
            "confidence": 0.0
        }