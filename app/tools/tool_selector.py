# app/tools/tool_selector.py
import json
from app.llm.factory import get_llm
from app.tools.tool_prompt import (
    TOOL_SELECTION_PROMPT
)

llm = get_llm()

def llm_select_tool(query):

    prompt = (
        TOOL_SELECTION_PROMPT
        .replace(
            "{query}",
            query
        )
    )

    response = llm.invoke(
        prompt
    )

    try:

        return json.loads(
            response
        )["tool"]

    except:

        return None