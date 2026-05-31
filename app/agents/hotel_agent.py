# hotel_agent.py

from langchain_core.messages import AIMessage

def hotel_agent(state):

    return {
        "hotel_results": "Sample Hotel Data",
        "messages": [
            AIMessage(content="Hotel Agent Executed")
        ]
    }