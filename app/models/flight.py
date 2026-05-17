from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Flight:
    id: int | None

    subscription_id: int | None

    origin: str
    destination: str

    departure_date: date | None
    return_date: date | None

    price: int
    currency: str

    provider: str | None = None

    deep_link: str | None = None

    stops: int = 0

    baggage_included: bool = False

    discovered_at: datetime | None = None