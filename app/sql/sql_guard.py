BLOCKED = [

    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "truncate"
]


def validate_sql(sql):

    sql_lower = sql.lower()

    for word in BLOCKED:

        if word in sql_lower:

            return False

    return True