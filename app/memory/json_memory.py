# app/memory/json_memory.py

import json
import os

from app.observability.metrics import (
    increment
)

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

MEMORY_FILE = os.path.join(
    DATA_DIR,
    "user_memory.json"
)


def load_memory():

    try:

        if not os.path.exists(
            MEMORY_FILE
        ):

            return {}

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

            if not content.strip():

                return {}

            return json.loads(
                content
            )

    except Exception as e:

        print(
            f"Memory Load Error: {e}"
        )

        return {}


def save_memory(
    memory
):

    try:

        os.makedirs(
            DATA_DIR,
            exist_ok=True
        )

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                memory,
                f,
                indent=4
            )

    except Exception as e:

        print(
            f"Memory Save Error: {e}"
        )


def set_memory(
    key,
    value
):

    memory = (
        load_memory()
    )

    memory[key] = value

    save_memory(
        memory
    )

    increment(
        "memory_updates"
    )


def get_memory(
    key
):

    memory = (
        load_memory()
    )

    return memory.get(
        key
    )


def get_all_memory():

    return load_memory()


def clear_memory():

    save_memory({})

    print(
        "Memory Cleared"
    )