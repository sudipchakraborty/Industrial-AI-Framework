from app.providers.openai_provider import (
    OpenAIProvider
)

provider = OpenAIProvider()


def generate_sql(question):

    prompt = f"""
You are an expert SQLite SQL generator.

Database Schema:

attendance(
    id INTEGER,
    emp_id TEXT,
    emp_name TEXT,
    date TEXT,
    check_in TEXT,
    status TEXT
)

Valid status values:

Present
Absent

Important Rules:

1. Generate SELECT statements only.
2. Never generate INSERT.
3. Never generate UPDATE.
4. Never generate DELETE.
5. Never generate DROP.
6. Never generate ALTER.
7. Use exact status values:
   - Present
   - Absent
8. Return SQL only.
9. Do not explain anything.
10. Do not use markdown.

Question:

{question}
"""

    sql = provider.generate(
        prompt
    )

    sql = (
        sql
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    # -----------------------------------
    # Normalize common LLM variations
    # -----------------------------------

    sql = sql.replace(
        "'absent'",
        "'Absent'"
    )

    sql = sql.replace(
        "'present'",
        "'Present'"
    )

    sql = sql.replace(
        '"absent"',
        '"Absent"'
    )

    sql = sql.replace(
        '"present"',
        '"Present"'
    )

    print(
        "\n[Generated SQL]"
    )

    print(sql)

    return sql