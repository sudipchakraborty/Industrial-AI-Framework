from app.observability.metrics import (
    increment
)


def request_approval(
    plan
):

    increment(
        "approval_requests"
    )

    print(
        "\nApproval Required"
    )

    print(
        "\nPlanned Actions:"
    )

    print(
        plan
    )

    choice = input(
        "\nApprove? (y/n): "
    )

    approved = (
        choice.lower() == "y"
    )

    if approved:

        increment(
            "approval_approved"
        )

    else:

        increment(
            "approval_rejected"
        )

    return approved