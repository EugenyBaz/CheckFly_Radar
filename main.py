import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from dotenv import load_dotenv

from app.bot.middlewares.access_middleware import AccessMiddleware
from app.bot.routers import setup_routers
from app.db.database import init_db
from app.db.seed import seed_airport_groups
from app.scheduler.flight_scheduler import run_scheduler

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main() -> None:
    init_db()
    seed_airport_groups()

    bot = Bot(token=BOT_TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="watch", description="Создать мониторинг"),
            BotCommand(command="list", description="Мои мониторинги"),
            BotCommand(command="cancel", description="Отменить ввод"),
            BotCommand(command="delete", description="Удалить мониторинг"),
        ]
    )
    dispatcher = Dispatcher()
    dispatcher.message.middleware(AccessMiddleware())
    dispatcher.include_router(setup_routers())
    asyncio.create_task(run_scheduler(bot))
    print("Bot started.")
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
