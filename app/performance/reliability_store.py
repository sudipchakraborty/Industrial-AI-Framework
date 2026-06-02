# app/performance/reliability_store.py

import json
from pathlib import Path

STORE_FILE = Path(
    "provider_accuracy.json"
)


def load_scores():

    if not STORE_FILE.exists():

        return {
            "openai": 1.0,
            "gemini": 1.0,
            "groq": 1.0,
            "ollama": 1.0
        }

    with open(
        STORE_FILE,
        "r"
    ) as f:

        return json.load(f)


def save_scores(scores):

    with open(
        STORE_FILE,
        "w"
    ) as f:

        json.dump(
            scores,
            f,
            indent=4
        )