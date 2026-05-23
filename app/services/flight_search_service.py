from datetime import datetime

from app.providers.travelpayouts_provider import TravelpayoutsProvider


class FlightSearchService:

    @staticmethod
    def search(subscription):

        flights = TravelpayoutsProvider.search_flights(
            origin=subscription.origin_group, destination=subscription.destination_group
        )

        matched_flights = []

        for flight in flights:

            departure_date = datetime.fromisoformat(flight["departure_at"]).date()

            if (
                departure_date < subscription.date_from
                or departure_date > subscription.date_to
            ):
                print(departure_date, subscription.date_from, subscription.date_to)
                continue

            if subscription.max_price and flight["price"] <= subscription.max_price:

                matched_flights.append(flight)

        return matched_flights
