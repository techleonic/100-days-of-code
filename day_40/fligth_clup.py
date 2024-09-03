import requests
import os
from data_manager import Fligth_storage
from google_fligths import fligth_google

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

# list of user in the google sheet
for user in list_of_users:
    fligth_search= fligth_google(departure=user["departureCode"],arrival=user["arrival"])
    all_flights = fligth_search.get_flights()["best_flights"]

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
                                        arrival=user["arrival"])
        flight_storage.save()

# GETS THE FLIGTHS WITH THE QUERY DEPARTURE AND ARRIVAL FROM USERS["DEPARTURE], USERS["ARRIVAL]