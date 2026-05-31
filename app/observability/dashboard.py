# app/observability/dashboard.py

from app.observability.metrics import (
    get_metrics
)


def show_dashboard():

    metrics = get_metrics()

    print("\n")
    print("=" * 50)
    print("ROUTING DASHBOARD")
    print("=" * 50)

    for key, value in metrics.items():

        print(
            f"{key:<30} : {value}"
        )

    print("=" * 50)