# app/tools/tool_selector.py

import json
import re

from app.llm.factory import (
    get_llm
)

from app.tools.tool_prompt import (
    TOOL_SELECTION_PROMPT
)

llm = get_llm()


# =====================================
# FAST RULE ROUTER
# =====================================

def fast_select_tool(query):

    query_lower = query.lower()

    # Flight

    if any(
        word in query_lower
        for word in [
            "flight",
            "ticket",
            "airline",
            "airport",
            "book flight"
        ]
    ):

        return "flight_search"

    # Hotel

    if any(
        word in query_lower
        for word in [
            "hotel",
            "room",
            "stay",
            "accommodation"
        ]
    ):

        return "hotel_search"

    # Weather

    if any(
        word in query_lower
        for word in [
            "weather",
            "temperature",
            "forecast",
            "rain"
        ]
    ):

        return "weather_search"

    return None


def _extract_json(response):

    try:

        return json.loads(
            response
        )

    except Exception:

        pass

    match = re.search(
        r"\{.*\}",
        response,
        re.DOTALL
    )

    if not match:

        raise ValueError(
            "No JSON found"
        )

    return json.loads(
        match.group()
    )


def llm_select_tool(query):

    # =====================================
    # PHASE-13 FAST PATH
    # =====================================

    tool = fast_select_tool(
        query
    )

    if tool:

        print(
            "\nFAST TOOL ROUTER:"
        )

        print(
            tool
        )

        return tool

    # =====================================
    # LLM FALLBACK
    # =====================================

    prompt = (
        TOOL_SELECTION_PROMPT
        .replace(
            "{query}",
            query
        )
    )

    try:

        response = llm.invoke(
            prompt
        )

        print(
            "\nTool Selector Response:"
        )

        print(
            response
        )

        result = _extract_json(
            response
        )

        return result.get(
            "tool"
        )

    except Exception as e:

        print(
            f"\nTool Selection Error: {e}"
        )

        return None