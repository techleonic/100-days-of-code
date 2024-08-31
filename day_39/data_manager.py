import os

import requests
APIKEY=os.getenv("APIKEY")
END_POINT = "https://api.sheety.co/cd1a064e0f44ab9c6aca48b4624dcb9a/flightDeals/prices"
class Fligth_storage():
    def __init__(self,airline,type,flight_class,duration,layovers=1,price=0):
        self.airline = airline
        self.type = type
        self.flight_class = flight_class
        self.duration = duration
        self.layovers = layovers
        self.price = price

    def save(self):
        sheety_params = {"price":{
            "airline": self.airline,
            "type": self.type,
            "class": self.flight_class,
            "duration":self.duration,
            "layovers": self.layovers,
            "price": self.price}
        }
        head = {
        "Authorization":APIKEY
        }
        result =  requests.post(url=END_POINT, json=sheety_params,headers=head)
        print(result.text)


# flight = Fligth_storage(airline="United picha",type="trip",flight_class="Business",duration=15.5,layovers=2,price=1500)
# flight.save()