from langchain_core.messages import HumanMessage
from app.graph.travel_graph import create_graph
####################################################
def main():

    print("===================================")
    print(" Travel Multi-Agent System ")
    print("===================================")

    app = create_graph()

    config = {
        "configurable": {
            "thread_id": "user1"
        }
    }

    while True:

        query = input("\nEnter Query (exit to quit): ")

        if query.lower() == "exit":
            break

        result = app.invoke(
            {
                "messages": [
                    HumanMessage(content=query)
                ],
                "user_query": query,
                "flight_results": "",
                "hotel_results": "",
                "itinerary": "",
                "llm_calls": 0
            },
            config=config
        )

        print("\n========== RESPONSE ==========\n")

        for msg in result["messages"]:
            print(msg.content)


if __name__ == "__main__":
    main()