from aiogram import Router
from app.bot.handlers.start import router as start_router
from app.bot.handlers.watch import router as watch_router
from app.bot.handlers.list_subscriptions import router as list_router
from app.bot.handlers.cancel import router as cancel
from app.bot.handlers.delete import router as delete_router


def setup_routers() -> Router:

    router = Router()
    router.include_router(start_router)
    router.include_router(watch_router)
    router.include_router(list_router)
    router.include_router(cancel)
    router.include_router(delete_router)

    return router
