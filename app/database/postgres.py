import psycopg
from psycopg.rows import dict_row

from langgraph.checkpoint.postgres import PostgresSaver

from app.config.settings import DATABASE_URL


def get_checkpointer():

    conn = psycopg.connect(
        DATABASE_URL,
        autocommit=True,
        row_factory=dict_row
    )

    checkpointer = PostgresSaver(conn)

    checkpointer.setup()

    return checkpointer