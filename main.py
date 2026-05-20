import asyncio
from aiogram import Bot, Dispatcher
from app.bot.routers import setup_routers
from app.db.database import init_db
import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main() -> None:
    init_db()


    bot = Bot(token=BOT_TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_router(setup_routers())
    print("Bot started.")
    await dispatcher.start_polling(bot)

if __name__ == "__main__": asyncio.run(main())
