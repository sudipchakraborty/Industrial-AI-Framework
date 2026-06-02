import sqlite3

conn = sqlite3.connect(
    "app/database/attendance.db"
)

cur = conn.cursor()

cur.execute(
    "SELECT * FROM attendance"
)

for row in cur.fetchall():
    print(row)

conn.close()