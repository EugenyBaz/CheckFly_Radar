from datetime import datetime


class TelegramAlertService:

    @staticmethod
    async def send_flight_alert(bot, telegram_id: int, flight: dict) -> None:

        departure = datetime.fromisoformat(flight["departure_at"])

        formatted_date = departure.strftime("%d-%m-%Y")

        formatted_time = departure.strftime("%H:%M")

        text = (
            f"✈️ Найден билет\n\n"
            f"{flight['origin']} → "
            f"{flight['destination']}\n\n"
            f"📅 Дата: {formatted_date}\n"
            f"🕒 Время: {formatted_time}\n"
            f"💰 Цена: "
            f"{flight['price']} "
            f"{flight['currency']}\n"
            f"🔁 Пересадки: "
            f"{flight['transfers']}\n"
            f"✈️ Provider: "
            f"{flight['provider']}\n\n"
            f"🔗 Открыть билет:\n"
            f"{flight['link']}"
        )

        await bot.send_message(chat_id=telegram_id, text=text)
