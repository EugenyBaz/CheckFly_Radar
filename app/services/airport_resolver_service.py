from app.db.database import (
    get_connection
)


class AirportResolverService:

    @staticmethod
    def resolve(
        text: str
    ) -> str:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT group_code
            FROM airport_group_aliases
            WHERE lower(alias) = ?
            """,
            (text.lower(),)
        )

        row = cursor.fetchone()

        connection.close()

        if row:

            return row["group_code"]

        return text.upper()
