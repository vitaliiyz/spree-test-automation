import os
from datetime import datetime, timedelta

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()


def get_user_by_email(email: str) -> dict | None:
    """
    Get user by email from spree_users table.
    """
    with psycopg.connect(
        os.environ["DATABASE_URL"],
        connect_timeout=5,
        autocommit=True,
        row_factory=dict_row,
    ) as conn:
        return conn.execute(
            """
            SELECT id, email, first_name, last_name
            FROM spree_users
            WHERE email = %s
            """,
            (email,),
        ).fetchone()


def get_spree_refresh_tokens_by_id(user_id: int) -> list[dict]:
    """
    Get spree_refresh_tokens by user_id from spree_refresh_tokens table.
    """

    with psycopg.connect(
        os.environ["DATABASE_URL"],
        connect_timeout=5,
        autocommit=True,
        row_factory=dict_row,
    ) as conn:
        return conn.execute(
            """
            SELECT * FROM spree_refresh_tokens WHERE user_id = %s
            """,
            (user_id,),
        ).fetchall()


def remove_created_user_data_by_id(user_id: int) -> None:
    """
    Remove created user data from spree_users and spree_refresh_tokens tables by user_id.
    """

    with psycopg.connect(
        os.environ["DATABASE_URL"],
        connect_timeout=5,
    ) as conn:
        conn.execute(
            """
            DELETE FROM spree_refresh_tokens WHERE user_id = %s
            """,
            (user_id,),
        )

        conn.execute(
            """
            DELETE FROM spree_users WHERE id = %s
            """,
            (user_id,),
        )


def create_user_data(email: str, first_name: str, last_name: str) -> None:
    """
    Create user data from spree_users table.
    """
    updated = datetime.now()
    created = updated - timedelta(minutes=30)

    with psycopg.connect(
        os.environ["DATABASE_URL"],
        connect_timeout=5,
        autocommit=True,
    ) as conn:
        conn.execute(
            """
            INSERT INTO spree_users (email, first_name, last_name, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s)""",
            (email, first_name, last_name, created, updated),
        )
