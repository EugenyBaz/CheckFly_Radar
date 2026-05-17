from sqlite3 import Row

from app.db.database import get_connection
from app.models.subscription import Subscription


class SubscriptionRepository:

    @staticmethod
    def create_subscription(
        subscription: Subscription
    ) -> Subscription:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO subscriptions (
                user_id,
                origin_group,
                destination_group,
                allow_moscow_transfer,
                date_from,
                date_to,
                adults,
                children,
                baggage_mode,
                max_price,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                subscription.user_id,
                subscription.origin_group,
                subscription.destination_group,
                subscription.allow_moscow_transfer,
                subscription.date_from,
                subscription.date_to,
                subscription.adults,
                subscription.children,
                subscription.baggage_mode,
                subscription.max_price,
                subscription.status
            )
        )

        connection.commit()

        subscription_id = cursor.lastrowid

        connection.close()

        subscription.id = subscription_id

        return subscription

    @staticmethod
    def get_active_subscriptions() -> list[Subscription]:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM subscriptions
            WHERE status = 'active'
            """
        )

        rows: list[Row] = cursor.fetchall()

        connection.close()

        subscriptions = []

        for row in rows:

            subscriptions.append(
                Subscription(
                    id=row["id"],
                    user_id=row["user_id"],
                    origin_group=row["origin_group"],
                    destination_group=row["destination_group"],
                    allow_moscow_transfer=bool(
                        row["allow_moscow_transfer"]
                    ),
                    date_from=row["date_from"],
                    date_to=row["date_to"],
                    adults=row["adults"],
                    children=row["children"],
                    baggage_mode=row["baggage_mode"],
                    max_price=row["max_price"],
                    status=row["status"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"]
                )
            )

        return subscriptions