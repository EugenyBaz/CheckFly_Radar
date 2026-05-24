from app.db.database import get_connection


class AlertRepository:

    @staticmethod
    def alert_exists(flight_hash: str) -> bool:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM alerts_sent
            WHERE flight_hash = ?
            """,
            (flight_hash,),
        )

        result = cursor.fetchone()

        connection.close()

        return result is not None

    @staticmethod
    def save_alert(subscription_id: int, flight_hash: str, sent_price: int) -> None:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO alerts_sent (
                subscription_id,
                flight_hash,
                sent_price
            )
            VALUES (?, ?, ?)
            """,
            (subscription_id, flight_hash, sent_price),
        )

        connection.commit()

        connection.close()
