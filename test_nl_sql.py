from dotenv import load_dotenv

load_dotenv()

from app.sql.sql_generator import (
    generate_sql
)

from app.database.sql_executor import (
    execute_sql
)

from app.sql.result_formatter import (
    format_results
)

query = "Who is absent today?"

sql = generate_sql(query)

rows = execute_sql(sql)

answer = format_results(
    query,
    rows
)

print(answer)