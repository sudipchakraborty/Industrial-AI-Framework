import sqlite3

DB_NAME = "industrial.db"

def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS machine_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        machine_id TEXT,
        temperature REAL,
        vibration REAL,
        current REAL,
        status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def insert_data(machine_id, temperature, vibration, current, status):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO machine_data
    (machine_id, temperature, vibration, current, status)
    VALUES (?, ?, ?, ?, ?)
    """, (machine_id, temperature, vibration, current, status))

    conn.commit()
    conn.close()


def get_latest_data():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT machine_id, temperature, vibration, current, status
    FROM machine_data
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    return row