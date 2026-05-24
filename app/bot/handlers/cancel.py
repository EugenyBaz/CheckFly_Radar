from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, StateFilter

router = Router()


@router.message(StateFilter("*"), Command("cancel"))
async def cancel_command(message: Message, state: FSMContext) -> None:

    current_state = await state.get_state()

    if current_state is None:

        await message.answer("Нет активного ввода.")

        return

    await state.clear()

    await message.answer("❌ Ввод отменён.")
