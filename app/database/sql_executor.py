import sqlite3

DB_PATH = "app/database/attendance.db"


def execute_sql(sql):

    conn = sqlite3.connect(
        DB_PATH
    )

    cur = conn.cursor()

    cur.execute(sql)

    rows = cur.fetchall()

    conn.close()

    return rows