import sqlite3

DB_PATH = "app/database/attendance.db"


class DatabaseManager:

    def get_connection(self):
        return sqlite3.connect(DB_PATH)

    def get_absent_today(self, today):

        conn = self.get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT emp_id, emp_name
            FROM attendance
            WHERE date=?
            AND status='Absent'
            """,
            (today,)
        )

        rows = cur.fetchall()

        conn.close()

        return rows

    def get_present_today(self, today):

        conn = self.get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT emp_id, emp_name
            FROM attendance
            WHERE date=?
            AND status='Present'
            """,
            (today,)
        )

        rows = cur.fetchall()

        conn.close()

        return rows

    def get_employee(self, emp_id):

        conn = self.get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT *
            FROM attendance
            WHERE emp_id=?
            ORDER BY date DESC
            """,
            (emp_id,)
        )

        rows = cur.fetchall()

        conn.close()

        return rows

    def get_late_today(self, today):

        conn = self.get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT emp_id, emp_name
            FROM attendance
            WHERE date=?
            AND check_in > '09:30'
            """,
            (today,)
        )

        rows = cur.fetchall()

        conn.close()

        return rows