from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.db.repositories.subscription_repository import (
    SubscriptionRepository,
)

from app.db.repositories.user_repository import (
    UserRepository,
)

router = Router()


@router.message(Command("list"))
async def list_command(message: Message) -> None:

    telegram_user = message.from_user

    user = UserRepository.get_by_telegram_id(telegram_user.id)

    if not user:

        await message.answer("У вас нет мониторингов.")

        return

    subscriptions = SubscriptionRepository.get_by_user_id(user.id)

    if not subscriptions:

        await message.answer("Активных мониторингов нет.")

        return

    response = "✈️ Активные мониторинги\n\n"

    for subscription in subscriptions:

        response += (
            f"ID: {subscription.id}\n"
            f"{subscription.origin_group} → "
            f"{subscription.destination_group}\n"
            f"{subscription.date_from} → "
            f"{subscription.date_to}\n"
            f"До {subscription.max_price} "
            f"{subscription.currency}\n\n"
        )

    await message.answer(response)
