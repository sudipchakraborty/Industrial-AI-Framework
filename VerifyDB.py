import sqlite3

conn = sqlite3.connect(
    "app/database/attendance.db"
)

cur = conn.cursor()

cur.execute(
    "SELECT DISTINCT status FROM attendance"
)

print(cur.fetchall())

conn.close()