# app/observability/dashboard.py

from app.observability.metrics import (
    METRICS
)

def show_dashboard():

    print(
        "\n"
        + "="*50
    )

    print(
        "OBSERVABILITY DASHBOARD"
    )

    print(
        "="*50
    )

    for k, v in (
        METRICS.items()
    ):

        print(
            f"{k:<30}: {v}"
        )

    print(
        "="*50
    )