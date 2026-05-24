import os

import httpx

from dotenv import load_dotenv

load_dotenv()


class TravelpayoutsProvider:

    BASE_URL = "https://api.travelpayouts.com"

    TOKEN = os.getenv("TRAVELPAYOUTS_TOKEN")

    @classmethod
    def search_flights(cls, origin: str, destination: str):

        response = httpx.get(
            f"{cls.BASE_URL}/aviasales/v3/prices_for_dates",
            params={
                "origin": origin,
                "destination": destination,
                "currency": "rub",
                "one_way": "true",
            },
            headers={"X-Access-Token": cls.TOKEN},
            timeout=20,
        )

        print(response.status_code)

        data = response.json()

        if not data.get("data"):

            return []

        flights = []

        for item in data["data"]:

            flights.append(
                {
                    "origin": item["origin"],
                    "destination": item["destination"],
                    "price": item["price"],
                    "currency": data["currency"].upper(),
                    "provider": "travelpayouts",
                    "departure_at": item["departure_at"],
                    "transfers": item["transfers"],
                    "link": (f"https://www.aviasales.ru" f"{item['link']}"),
                }
            )
        print(f"Flights found: " f"{len(data['data'])}")
        return flights

