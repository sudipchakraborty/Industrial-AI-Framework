# app/utils/query_classifier.py

GENERAL_PATTERNS = [

    "capital",
    "who is",
    "what is",
    "when is",
    "where is",
    "why",
    "how",
]


def is_general_query(query):

    query = query.lower()

    return any(
        pattern in query
        for pattern in GENERAL_PATTERNS
    )