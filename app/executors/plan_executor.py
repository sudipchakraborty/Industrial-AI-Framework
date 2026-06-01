import time


def execute_step(
    step_name,
    func,
    *args
):

    retries = 3

    for attempt in range(
        retries
    ):

        try:

            return func(
                *args
            )

        except Exception as e:

            print(
                f"{step_name} failed "
                f"attempt {attempt+1}"
            )

            time.sleep(1)

    return {
        "error":
        f"{step_name} failed"
    }