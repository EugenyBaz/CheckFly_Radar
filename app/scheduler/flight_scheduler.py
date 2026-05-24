import asyncio

from app.db.repositories.subscription_repository import (
    SubscriptionRepository,
)

from app.services.flight_search_service import (
    FlightSearchService,
)
from app.db.repositories.alert_repository import (
    AlertRepository,
)
from app.db.repositories.user_repository import (
    UserRepository,
)
from app.services.telegram_alert_service import (
    TelegramAlertService,
)


async def run_scheduler(bot):
    while True:

        print("Scheduler tick...")

        subscriptions = SubscriptionRepository.get_active_subscriptions()

        for subscription in subscriptions:
            try:
                flights = (await FlightSearchService.search(subscription))

            except Exception as e:

                print(f"Scheduler error: {e}")
                continue

            for flight in flights:
                flight_hash = (
                    f"{flight['origin']}-"
                    f"{flight['destination']}-"
                    f"{flight['price']}"
                )

                already_sent = AlertRepository.alert_exists(flight_hash)
                if already_sent:
                    continue

                user = UserRepository.get_by_id(subscription.user_id)

                if not user:
                    continue
                await TelegramAlertService.send_flight_alert(
                    bot=bot, telegram_id=user.telegram_id, flight=flight
                )

                AlertRepository.save_alert(
                    subscription_id=subscription.id,
                    flight_hash=flight_hash,
                    sent_price=flight["price"],
                )
                print(f"Alert sent: {flight_hash}")

        await asyncio.sleep(300)
