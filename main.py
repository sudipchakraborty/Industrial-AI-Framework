# main.py

from app.routers.supervisor import (
    supervisor
)

from app.observability.dashboard import (
    show_dashboard
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

    while True:

        query = input(
            "User: "
        ).strip()

        # ==========================
        # EXIT
        # ==========================

        if (
            query.lower()
            == "exit"
        ):

            print(
                "\nGoodbye!"
            )

            break

        # ==========================
        # DASHBOARD
        # ==========================

        if (
            query.lower()
            in [
                "dashboard",
                "metrics"
            ]
        ):

            show_dashboard()

            continue

        # ==========================
        # EMPTY INPUT
        # ==========================

        if not query:

            continue

        # ==========================
        # SUPERVISOR
        # ==========================

        try:

            response = supervisor(
                query
            )

            print(
                response
            )

        except Exception as e:

            print(
                "\nExecution Error:"
            )

            print(
                str(e)
            )


if __name__ == "__main__":

    main()