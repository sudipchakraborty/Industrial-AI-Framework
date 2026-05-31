# flight_agent.py

from langchain_core.messages import AIMessage

def flight_agent(state):

    return {
        "flight_results": "Sample Flight Data",
        "messages": [
            AIMessage(content="Flight Agent Executed")
        ]
    }