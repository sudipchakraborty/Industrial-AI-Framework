from app.providers.openai_provider import (
    OpenAIProvider
)

provider = OpenAIProvider()


def format_results(
    question,
    rows
):

    if not rows:

        return (
            "No records found."
        )

    prompt = f"""
Question:

{question}

Database Results:

{rows}

Create a concise and user-friendly answer.

Rules:

1. Do not mention SQL.
2. Do not mention databases.
3. Use bullet points if needed.
4. Keep answer short.
"""

    return provider.generate(
        prompt,
        max_tokens=200
    )