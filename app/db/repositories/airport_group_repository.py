from sqlite3 import Row

from app.db.database import get_connection


class AirportGroupRepository:

    @staticmethod
    def get_airports_by_group(group_code: str) -> list[str]:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT airport_code
            FROM airport_group_members
            WHERE group_code = ?
            """,
            (group_code,),
        )

        rows: list[Row] = cursor.fetchall()

        connection.close()

        return [row["airport_code"] for row in rows]
