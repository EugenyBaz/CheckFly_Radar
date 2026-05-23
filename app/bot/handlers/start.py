from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.services.user_service import UserService

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    telegram_user = message.from_user

    user = UserService.get_or_create_user(
        telegram_id=telegram_user.id, username=telegram_user.username
    )
    await message.answer(
        f"Welcome to CheckFly Radar ✈️\n" f"User registered: {user.username}"
    )
