import os

from twilio.rest import Client
import requests
from data_manager import APIKEY,END_POINT

def send_notification():
    # GETS A LIST OF FLIGHTS FROM GOOGLE SHEETS
    head = {
    "Authorization":APIKEY
    }
    result = requests.get(url=END_POINT, headers=head )
    list_of_flights = result.json()["prices"]

    # NOTIFIES THE CLIENT FOR THE TOP TOW
    account_sid = os.getenv("TWILIO_SSID")
    token = os.getenv("TWILIO_TOKEN")
    client= Client(account_sid,token)
    for flight in list_of_flights[0:2]:
        message = client.messages.create(
            from_="+19787231024",
            body= f"airline: {flight["airline"]}\ntype: {flight["type"]}\nclass: {flight["class"]}\n"+
                  f"duration: {flight["duration"]}HRS\nlayovers: {flight["layovers"]}\nprice: {flight["price"]}$\n",
            to="+50586287283"
        )

"""
{
      "airline": "United",
      "type": "Round trip",
      "class": "Economy",
      "duration": 33.75,
      "layovers": 2,
      "price": 1584,
      "id": 2
    },
"""
