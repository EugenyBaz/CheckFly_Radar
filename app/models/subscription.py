from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Subscription:
    id: int | None

    user_id: int

    origin_group: str
    destination_group: str

    allow_moscow_transfer: bool = True

    date_from: date | None = None
    date_to: date | None = None

    adults: int = 1
    children: int = 0

    baggage_mode: str = "checked"

    max_price: int | None = None

    currency: str = "RUB"

    status: str = "active"

    created_at: datetime | None = None
    updated_at: datetime | None = None
