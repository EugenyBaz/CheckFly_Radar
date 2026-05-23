from app.providers.travelpayouts_provider import TravelpayoutsProvider

data = TravelpayoutsProvider.search_flights(origin="LED", destination="AYT")

print(data)
