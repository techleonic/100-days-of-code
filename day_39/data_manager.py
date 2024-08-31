import requests
class Fligth_storage():
    def __init__(self,airline,type,flight_class,duration,layovers,price):
        self.airline = airline
        self.type = type
        self.flight_class = flight_class
        self.duration = duration
        self.layovers = layovers
        self.price = price

    def save(self):

