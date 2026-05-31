from langchain_core.messages import HumanMessage

from app.llm.groq_client import llm

def general_agent(state):

    response = llm.invoke([
        HumanMessage(
            content=state["user_query"]
        )
    ])

    return {
        "messages": [response]
    }