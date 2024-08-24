import requests
import  os
api_key = os.getenv("AMADEUS_APIKEY")
api_secretkey = os.getenv("API_SECRETKEY")
TOKEN = os.getenv("TOKEN")
ENDPOINT_GET = "https://test.api.amadeus.com/v1/reference-data/locations/cities?countryCode=FR&keyword=PARIS&max=10"
q = "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=FRA&destinationLocationCode=BKK&departureDate=2024-12-31&adults=1&nonStop=false&max=10"
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(url=q,headers=headers)
response.raise_for_status()
print(response.json())