from app.routers.supervisor import supervisor

from app.observability.dashboard import (
    show_dashboard
)

while True:

    query = input("User: ")

    if query.lower() == "exit":

        show_dashboard()
        break

    response = supervisor(query)

    print(response)