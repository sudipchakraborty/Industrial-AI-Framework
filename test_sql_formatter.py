from dotenv import load_dotenv

load_dotenv()

from app.sql.result_formatter import (
    format_results
)

rows = [

    ("E1002", "Amit"),

    ("E1004", "Priya")
]

answer = format_results(

    "Who is absent today?",

    rows
)

print(answer)