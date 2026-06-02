from dotenv import load_dotenv

load_dotenv()

from app.sql.sql_generator import (
    generate_sql
)

from app.database.sql_executor import (
    execute_sql
)

query = "Who is absent today?"

sql = generate_sql(query)

print("\nGenerated SQL:\n")
print(sql)

rows = execute_sql(sql)

print("\nResults:\n")
print(rows)