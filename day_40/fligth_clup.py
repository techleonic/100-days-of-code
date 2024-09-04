import requests
import os
import data_manager
from data_manager import Fligth_storage
from google_fligths import fligth_google
import smtplib

USER_ENDPOINT = "https://api.sheety.co/cd1a064e0f44ab9c6aca48b4624dcb9a/emails/respuestasDeFormulario1"
USER_TOKEN = os.getenv("EMAILS_TOKEN")
print(USER_TOKEN)
user_head = {
    "Authorization": USER_TOKEN
}

# gets the list of user with email and departure and arrival
results = requests.get(url=USER_ENDPOINT, headers=user_head)
results.raise_for_status()
list_of_users = results.json()["respuestasDeFormulario1"]

#TODO: DELETE OLD FLIGTHS FROM YESTARDAY
# data_manager.delete_old_fligths()


# GET USERS DEPARTURE AND ARRIVAL AND POPULATES THE FLIGHTS GOOGLE SHEETS
# list of user in the google sheet

for user in list_of_users:
    fligth_search= fligth_google(departure=user["departureCode"],arrival=user["arrival"])
    data = fligth_search.get_flights()
    all_flights = data["best_flights"]
    # SAVE ALL FLIGHTS IN GOOGLE SHEET
    for flight in all_flights:
        try:
            layovers = len(flight["layovers"])
        except KeyError:
            layovers = 0
        flight_storage = Fligth_storage(airline=flight["flights"][0]["airline"],
                                        type=flight["type"],
                                        flight_class=flight["flights"][0]["travel_class"],
                                        duration=round(int(flight["total_duration"]) / 60, 2),
                                        layovers=layovers,
                                        price=flight["price"],
                                        departure=user["departureCode"],
                                        arrival=user["arrival"],
                                        outbound=data["search_parameters"]["outbound_date"],
                                        freturn=data["search_parameters"]["return_date"]
                                        )
        flight_storage.save()

# TODO: GETS THE FLIGTHS WITH THE QUERY DEPARTURE AND ARRIVAL FROM USERS["DEPARTURE], USERS["ARRIVAL]
sender =  os.getenv("SENDER")
password = os.getenv("PASSWORD")
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender, password)
for user in list_of_users:
    message = ''
    text=''
    list_filter_flights = data_manager.get_flights_destination(departure=user["departureCode"],arrival=user["arrival"])
    for filter_flight  in list_filter_flights:
        text+= f"Airline: {filter_flight["airline"]}\nType: {filter_flight["type"]}\nClass: {filter_flight["class"]}\nDuration: {filter_flight["duration"]}HRS\nlayovers: {filter_flight["layovers"]}\nprice: {filter_flight["price"]}$\nDeparture: {filter_flight["departure"]}\nArrival: {filter_flight["arrival"]}\n\n"
    message = 'Subject: {}\n\n{}'.format("Airline Information", text)
    print(message)
    server.sendmail(sender,user["email"],message)
server.quit()