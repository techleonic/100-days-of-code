import requests
import  os

class fligth_search:
    def __init__(self,max_price,origin):
        self.max_price = max_price
        self.origin = origin
        self.get_Data()

    # QUERIES FOR AMEDEUS
    ENDPOINT_GET = "https://test.api.amadeus.com/v1/reference-data/locations/cities?countryCode=FR&keyword=PARIS&max=10"
    q = "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=FRA&destinationLocationCode=BKK&departureDate=2024-12-31&adults=1&nonStop=false&max=5"
    ENDPOINT_KEY = "https://test.api.amadeus.com/v1/security/oauth2/token"

    #head post
    head_post = {
    "Content-Type": "application/x-www-form-urlencoded"
    }

    body = {
    "grant_type":"client_credentials",
    "client_id":os.getenv("AMADEUS_APIKEY"),
    "client_secret":os.getenv("AMADEUS_SECRETKEY"),
    }
    def get_Data(self):
        """gets the key to gain access to amadeus and returns a json data with the given prince a date"""
        response = requests.post(url=self.ENDPOINT_KEY,headers=self.head_post, data=self.body)
        print(response.json())
        data_access = response.json()
        token_type = data_access["token_type"]
        access_token = data_access["access_token"]

        print(token_type)
        print(access_token)
        ulr_q = f"https://test.api.amadeus.com/v1/shopping/flight-destinations?origin={str(self.origin)}&maxPrice={str(self.max_price)}"
        print(ulr_q)
        search_head = {
        "Authorization":f"{token_type} {access_token}"
        }
        search_response = requests.get(url=ulr_q, headers=search_head)
        print(search_response.json())

fligth_search(500,"PAR")