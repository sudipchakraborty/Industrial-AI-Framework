import json
from pathlib import Path

STOP_WORDS = {

    "need",
    "want",
    "please",
    "help",
    "with",
    "for",
    "the",
    "a",
    "an",
    "is",
    "are",
    "to",
    "of"
}

LEARNING_FILE = (
    Path(__file__).parent
    / "learned_keywords.json"
)


def load_learning():

    if not LEARNING_FILE.exists():

        return {}

    try:

        with open(
            LEARNING_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return {}


def save_learning(data):

    with open(
        LEARNING_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def learn(
    query,
    agent_name
):

    words = [

    word.lower()

    for word in query.split()

    if (
        len(word) > 3
        and
        word.lower()
        not in STOP_WORDS
    )
        ]

    data = load_learning()

    if agent_name not in data:

        data[agent_name] = []

    for word in words:

        if word not in data[agent_name]:

            data[agent_name].append(
                word
            )

    save_learning(data)