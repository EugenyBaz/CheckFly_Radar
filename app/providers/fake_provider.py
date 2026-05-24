import random


class FakeFlightProvider:

    @staticmethod
    def search_flights():
        return [
            {
                "origin": "SPB",
                "destination": "TURKEY_COAST",
                "price": random.randint(25000, 45000),
                "currency": "RUB",
                "provider": "fake_provider",
            }
        ]
