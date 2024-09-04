import os

import requests
from datetime import datetime
APIKEY=os.getenv("FLIGHT_TOKEN")
END_POINT = "https://api.sheety.co/cd1a064e0f44ab9c6aca48b4624dcb9a/flightDeals/prices"
head = {
        "Authorization":APIKEY
        }
class Fligth_storage():
    def __init__(self,airline,type,flight_class,duration,departure, arrival,outbound,freturn,layovers=1,price=0,):
        self.airline = airline
        self.type = type
        self.flight_class = flight_class
        self.duration = duration
        self.layovers = layovers
        self.price = price
        self.departure = departure
        self.arrival = arrival
        self.outbound = outbound
        self.freturn = freturn

    def save(self):
        sheety_params = {"price":{
            "airline": self.airline,
            "type": self.type,
            "class": self.flight_class,
            "duration":self.duration,
            "layovers": self.layovers,
            "price": self.price,
            "departure":self.departure,
            "arrival":self.arrival,
            "outboundDate":self.outbound,
            "returnDate":self.freturn
        }
        }

        result =  requests.post(url=END_POINT, json=sheety_params,headers=head)
def delete_old_fligths():
    flights_list = requests.get(url=END_POINT,headers=head)
    old_flights = flights_list.json()["prices"]
    if not old_flights:
        print("there is no flights in storage")
    else:
        for flights in old_flights:
            deleted_results = requests.delete(url=END_POINT+f"/{flights["id"]}", headers=head)
            print(deleted_results.text)
def get_flights_destination(departure,arrival):
    filter_endpoint = END_POINT+f"?filter[departure]={departure}&filter[arrival]={arrival}"
    filter_results = requests.get(url=filter_endpoint,headers=head)
    return filter_results.json()["prices"]
# flight = Fligth_storage(airline="United picha",type="trip",flight_class="Business",duration=15.5,layovers=2,price=1500)
# flight.save()