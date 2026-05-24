from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message

from app.db.repositories.subscription_repository import (
    SubscriptionRepository
)

from app.services.user_service import (
    UserService
)


router = Router()


@router.message(StateFilter("*"), Command("delete"))
async def delete_command(
    message: Message
) -> None:

    args = message.text.split()

    if len(args) != 2:

        await message.answer(
            "Чтобы удалить мониторинг напишите :\n"
            "/delete и рядом номер ID мониторинга.\n Например /delete 11"
        )

        return

    try:
        subscription_id = int(
            args[1]
        )

    except ValueError:

        await message.answer(
            "ID должен быть числом."
        )

        return

    telegram_user = message.from_user

    user = UserService.get_or_create_user(
        telegram_id=telegram_user.id,
        username=telegram_user.username
    )

    subscriptions = (
        SubscriptionRepository.get_by_user_id(
            user.id
        )
    )

    subscription_ids = [
        subscription.id
        for subscription in subscriptions
    ]

    if subscription_id not in subscription_ids:

        await message.answer(
            "Мониторинг не найден."
        )

        return

    SubscriptionRepository.delete_subscription(
        subscription_id
    )

    await message.answer(
        f"❌ Мониторинг "
        f"{subscription_id} удалён."
    )

