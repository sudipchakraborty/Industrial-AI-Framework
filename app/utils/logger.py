# app/utils/logger.py

from datetime import datetime
from pathlib import Path


LOG_FILE = (
    Path(__file__).resolve().parent.parent
    / "logs"
    / "routing.log"
)


def log_route(query, source, result):

    LOG_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{datetime.now()} | "
            f"{query} | "
            f"{source} | "
            f"{result}\n"
        )