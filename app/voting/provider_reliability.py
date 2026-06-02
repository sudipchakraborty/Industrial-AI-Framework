# app/voting/provider_reliability.py

PROVIDER_WEIGHTS = {

    "openai": 1.00,

    "groq": 0.95,

    "gemini": 0.90,

    "ollama": 0.85
}


def get_weight(provider):

    return PROVIDER_WEIGHTS.get(
        provider.lower(),
        0.75
    )