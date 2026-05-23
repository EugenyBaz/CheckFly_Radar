from datetime import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.bot.states.watch import WatchFlightState
from app.db.repositories.subscription_repository import (
    SubscriptionRepository,
)
from app.models.subscription import Subscription
from app.services.user_service import UserService

router = Router()


@router.message(Command("watch"))
async def watch_command(message: Message, state: FSMContext) -> None:
    await state.set_state(WatchFlightState.origin)

    await message.answer("Введите группу вылета (SPB/MOSCOW)")


@router.message(WatchFlightState.origin)
async def process_origin(message: Message, state: FSMContext) -> None:
    await state.update_data(origin=message.text.strip().upper())

    await state.set_state(WatchFlightState.destination)

    await message.answer("Введите направление (TURKEY_COAST):")


@router.message(WatchFlightState.destination)
async def process_destination(message: Message, state: FSMContext) -> None:
    await state.update_data(destination=message.text.strip().upper())

    await state.set_state(WatchFlightState.date_from)

    await message.answer("Введите дату начала (DD-MM-YYYY):")


@router.message(WatchFlightState.date_from)
async def process_date_from(message: Message, state: FSMContext) -> None:
    try:
        parsed_date = datetime.strptime(message.text, "%d-%m-%Y")
    except ValueError:
        await message.answer("❌ Неверный формат даты\n" "Используйте: 15-06-2026")
        return

    await state.update_data(date_from=parsed_date.date())

    await state.set_state(WatchFlightState.date_to)

    await message.answer("Введите дату конца (DD-MM-YYYY):")


@router.message(WatchFlightState.date_to)
async def process_date_to(message: Message, state: FSMContext) -> None:
    try:
        parsed_date = datetime.strptime(message.text, "%d-%m-%Y")
    except ValueError:
        await message.answer("❌ Неверный формат даты\n" "Используйте: 15-06-2026")
        return

    data = await state.get_data()
    date_from = data["date_from"]
    if parsed_date.date() < date_from:
        await message.answer("❌ Дата конца не может быть раньше даты начала")
        return

    await state.update_data(date_to=parsed_date.date())

    await state.set_state(WatchFlightState.max_price)

    await message.answer("Введите максимальную цену:")


@router.message(WatchFlightState.max_price)
async def process_max_price(message: Message, state: FSMContext) -> None:
    try:
        max_price = int(message.text)
    except ValueError:
        await message.answer("❌ Цена должна быть числом\n" "Например: 30000")
        return
    if max_price <= 0:
        await message.answer("❌ Цена должна быть больше 0")
        return

    data = await state.get_data()

    telegram_user = message.from_user
    user = UserService.get_or_create_user(
        telegram_id=telegram_user.id, username=telegram_user.username
    )

    subscription = Subscription(
        id=None,
        user_id=user.id,
        origin_group=data["origin"],
        destination_group=data["destination"],
        date_from=data["date_from"],
        date_to=data["date_to"],
        max_price=max_price,
        currency="RUB",
    )

    SubscriptionRepository.create_subscription(subscription)

    await message.answer(
        f"✈️ Мониторинг создан\n\n"
        f"Маршрут:\n"
        f"{data['origin']} → {data['destination']}\n\n"
        f"Даты:\n"
        f"{data['date_from'].strftime('%d-%m-%Y')} → {data['date_to'].strftime('%d-%m-%Y')}\n\n"
        f"Максимальная цена:\n"
        f"{max_price} RUB"
    )

    await state.clear()
