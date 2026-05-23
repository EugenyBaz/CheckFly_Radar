import os

from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv(
    "BOT_TOKEN"
)

TRAVELPAYOUTS_TOKEN = os.getenv(
    "TRAVELPAYOUTS_TOKEN"
)

ALLOWED_TELEGRAM_IDS = [
    int(user_id)
    for user_id in os.getenv(
        "ALLOWED_TELEGRAM_IDS",
        ""
    ).split(",")
    if user_id
]

