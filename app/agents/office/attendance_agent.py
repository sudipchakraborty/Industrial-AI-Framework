import re
from datetime import date

from app.database.db_manager import (
    DatabaseManager
)

from app.sql.sql_generator import (
    generate_sql
)

from app.sql.sql_guard import (
    validate_sql
)

from app.database.sql_executor import (
    execute_sql
)

from app.sql.result_formatter import (
    format_results
)


class AttendanceAgent:

    def __init__(self):

        self.db = DatabaseManager()

    def execute(
        self,
        query
    ):

        query_lower = query.lower()

        today = str(
            date.today()
        )

        # =====================================
        # FAST PATH
        # =====================================

        if "absent" in query_lower:

            rows = self.db.get_absent_today(
                today
            )

            if not rows:

                return (
                    "No absent employees today."
                )

            result = []

            for emp_id, emp_name in rows:

                result.append(
                    f"{emp_id} - {emp_name}"
                )

            return (
                "Absent Employees:\n"
                + "\n".join(result)
            )

        if "present" in query_lower:

            rows = self.db.get_present_today(
                today
            )

            if not rows:

                return (
                    "No present employees today."
                )

            result = []

            for emp_id, emp_name in rows:

                result.append(
                    f"{emp_id} - {emp_name}"
                )

            return (
                "Present Employees:\n"
                + "\n".join(result)
            )

        if "late" in query_lower:

            rows = self.db.get_late_today(
                today
            )

            return (
                f"Late Employees: {len(rows)}"
            )

        emp_match = re.search(
            r"(E\d+)",
            query,
            re.IGNORECASE
        )

        if emp_match:

            emp_id = (
                emp_match.group(1)
                .upper()
            )

            rows = self.db.get_employee(
                emp_id
            )

            if not rows:

                return (
                    f"No attendance records found "
                    f"for {emp_id}"
                )

            output = []

            for row in rows:

                output.append(
                    f"""
Employee ID : {row[1]}
Name        : {row[2]}
Date        : {row[3]}
Check In    : {row[4]}
Status      : {row[5]}
"""
                )

            return "\n".join(
                output
            )

        # =====================================
        # PHASE-16C
        # NATURAL LANGUAGE → SQL
        # =====================================

        try:

            sql = generate_sql(
                query
            )

            if not validate_sql(
                sql
            ):

                return (
                    "Unsafe SQL blocked."
                )

            rows = execute_sql(
                sql
            )

            return format_results(
                query,
                rows
            )

        except Exception as e:

            return (
                f"SQL execution failed: "
                f"{str(e)}"
            )