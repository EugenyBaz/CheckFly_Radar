from datetime import datetime
import asyncio

from app.providers.travelpayouts_provider import (
    TravelpayoutsProvider
)

from app.db.repositories.airport_group_repository import (
    AirportGroupRepository
)


class FlightSearchService:

    @staticmethod
    async def search(subscription):

        matched_flights = []

        origin_airports = (
            AirportGroupRepository
            .get_airports_by_group(
                subscription.origin_group
            )
        )

        destination_airports = (
            AirportGroupRepository
            .get_airports_by_group(
                subscription.destination_group
            )
        )

        for origin in origin_airports:

            for destination in destination_airports:

                await asyncio.sleep(0)

                print(
                    f"Searching: "
                    f"{origin} → {destination}"
                )

                flights = (
                    TravelpayoutsProvider
                    .search_flights(
                        origin=origin,
                        destination=destination
                    )
                )

                for flight in flights:

                    departure_date = (
                        datetime.fromisoformat(
                            flight["departure_at"]
                        ).date()
                    )

                    if (
                        departure_date
                        < subscription.date_from
                        or departure_date
                        > subscription.date_to
                    ):

                        continue

                    if (
                        subscription.max_price
                        and flight["price"]
                        <= subscription.max_price
                    ):

                        matched_flights.append(
                            flight
                        )

        return matched_flights




