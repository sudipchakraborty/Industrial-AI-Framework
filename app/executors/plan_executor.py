import time

from app.observability.metrics import (
    increment
)


def execute_step(
    step_name,
    func,
    *args
):

    retries = 3

    increment(
        "tool_calls"
    )

    for attempt in range(
        retries
    ):

        try:

            return func(
                *args
            )

        except Exception as e:

            increment(
                "tool_failures"
            )

            print(
                f"{step_name} failed "
                f"attempt {attempt + 1}"
            )

            print(
                f"Error: {e}"
            )

            time.sleep(
                1
            )

    return {

        "error":
            f"{step_name} failed after "
            f"{retries} retries"
    }