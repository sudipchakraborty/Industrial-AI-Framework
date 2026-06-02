from dotenv import load_dotenv

load_dotenv()

from app.sql.sql_generator import (
    generate_sql
)



sql = generate_sql(
    "Who is absent today?"
)

print(sql)