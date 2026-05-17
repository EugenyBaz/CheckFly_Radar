from sqlite3 import Row

from app.db.database import get_connection
from app.models.user import User


class UserRepository:

    @staticmethod
    def create_user(
        telegram_id: int,
        username: str | None = None
    ) -> User:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO users (
                telegram_id,
                username
            )
            VALUES (?, ?)
            """,
            (telegram_id, username)
        )

        connection.commit()

        user_id = cursor.lastrowid

        connection.close()

        return User(
            id=user_id,
            telegram_id=telegram_id,
            username=username
        )

    @staticmethod
    def get_by_telegram_id(
        telegram_id: int
    ) -> User | None:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE telegram_id = ?
            """,
            (telegram_id,)
        )

        row: Row | None = cursor.fetchone()

        connection.close()

        if row is None:
            return None

        return User(
            id=row["id"],
            telegram_id=row["telegram_id"],
            username=row["username"],
            created_at=row["created_at"]
        )