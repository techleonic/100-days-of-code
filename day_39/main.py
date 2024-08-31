from   google_fligths import fligth_google
from data_manager import Fligth_storage
# load the json from api
data = fligth_google("MGA","CDG",)
flights_list = data.get_flights()

#join all the flights in a list
all_flights = flights_list["best_flights"] + flights_list["other_flights"]

# for each flight
for flight in all_flights:
    print(len(all_flights))
    flight_storage = Fligth_storage(airline=flight["flights"][0]["airline"],
                                    type=flight["type"],
                                    flight_class=flight["flights"][0]["travel_class"],
                                    duration=round( int(flight["total_duration"])/60,2),
                                    layovers=len(flight["layovers"]),
                                    price=flight["price"])
    flight_storage.save()
    # print(flight["flights"][0]["airline"],flight["type"],flight["flights"][0]["travel_class"],round( int(flight["total_duration"])/60,2),len(flight["layovers"]),flight["price"])





# result.json()["best_flights"][1]["flights"][0]["departure_airport"]
# print(["best_flights"][1]["price"])