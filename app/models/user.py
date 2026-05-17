from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int | None
    telegram_id: int
    username: str | None
    created_at: datetime | None = None