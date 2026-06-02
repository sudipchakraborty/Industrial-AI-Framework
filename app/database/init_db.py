import sqlite3

conn = sqlite3.connect(
    "app/database/attendance.db"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_id TEXT,
    emp_name TEXT,
    date TEXT,
    check_in TEXT,
    status TEXT
)
""")

sample_data = [

    ("E1001","Rahul","2026-06-02","09:05","Present"),
    ("E1002","Amit","2026-06-02",None,"Absent"),
    ("E1003","John","2026-06-02","10:15","Present"),
    ("E1004","Priya","2026-06-02",None,"Absent")
]

cur.executemany(
    """
    INSERT INTO attendance(
        emp_id,
        emp_name,
        date,
        check_in,
        status
    )
    VALUES(?,?,?,?,?)
    """,
    sample_data
)

conn.commit()
conn.close()

print("Attendance DB Created")