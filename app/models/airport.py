from dataclasses import dataclass


@dataclass
class AirportGroup:
    id: int | None

    code: str
    name: str
