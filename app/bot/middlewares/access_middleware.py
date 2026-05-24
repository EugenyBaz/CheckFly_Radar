from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from app.config import ALLOWED_TELEGRAM_IDS


class AccessMiddleware(BaseMiddleware):

    async def __call__(self, handler, event: TelegramObject, data):

        telegram_user = getattr(event, "from_user", None)

        if telegram_user is None or telegram_user.id not in ALLOWED_TELEGRAM_IDS:

            if hasattr(event, "answer"):

                await event.answer("⛔ Access denied")

            return

        return await handler(event, data)
