from   google_fligths import fligth_google

# load the json from api
data = fligth_google("MGA","CDG",)
flights_list = data.get_flights()

#join all the fligths in a list
all_flights = flights_list["best_flights"] + flights_list["other_flights"]

for flight in all_flights:
    print(flight["flights"][0]["airline"],flight["type"],flight["flights"][0]["travel_class"],round( int(flight["total_duration"])/60,2),len(flight["layovers"]),flight["price"])

# result.json()["best_flights"][1]["flights"][0]["departure_airport"]

# print(["best_flights"][1]["price"])