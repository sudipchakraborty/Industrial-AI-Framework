# main.py

import os
import time
from dotenv import load_dotenv

load_dotenv()

#############################
print(
    "OPENAI:",
    bool(
        os.getenv(
            "OPENAI_API_KEY"
        )
    )
)

print(
    "GROQ:",
    bool(
        os.getenv(
            "GROQ_API_KEY"
        )
    )
)
######################





from app.routers.supervisor import supervisor
from app.observability.dashboard import (
    show_dashboard
)

from app.agents.registry_loader import (
    get_registry
)


def main():

    print(
        "\nIndustrial AI Framework Started"
    )

    print(
        "Type 'dashboard' to view metrics"
    )

    print(
        "Type 'exit' to quit\n"
    )

    print("\nREGISTRY:\n")

    for k in get_registry().keys():
        print(k)

    while True:

        query = input(
            "User: "
        ).strip()

        # ==========================
        # EXIT
        # ==========================

        if query.lower() == "exit":

            print(
                "\nGoodbye!"
            )

            break

        # ==========================
        # DASHBOARD
        # ==========================

        if query.lower() in [
            "dashboard",
            "metrics"
        ]:

            show_dashboard()

            continue

        # ==========================
        # EMPTY INPUT
        # ==========================

        if not query:

            continue

        try:

            start_time = time.time()

            response = supervisor(
                query
            )

            elapsed = round(
                time.time() - start_time,
                2
            )

            print("\nAssistant:")

            print(response)

            print(
                f"\nExecution Time: {elapsed}s"
            )

        except Exception as e:

            print(
                "\nExecution Error:"
            )

            print(str(e))


if __name__ == "__main__":

    main()