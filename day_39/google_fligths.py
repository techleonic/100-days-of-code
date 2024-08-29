import requests
import os
from datetime import datetime,timedelta

class fligth_google():
    def __init__(self,departure,arrival,output_date = datetime.now().strftime("%Y-%m-%d"),
    return_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")):
        self.departure = departure
        self.arrival = arrival
        self.output_date = output_date
        self.return_date = return_date
        self.end_point = "https://serpapi.com/search?engine=google_flights"
        self.get_flights()
    def get_flights(self):
        params = {"engine":"google_flights",
                  "api_key": os.getenv("SerApi"),
                  "departure_id":self.departure,"arrival_id":self.arrival,
                  "outbound_date":self.output_date,"return_date":self.return_date}
        result = requests.get(url=self.end_point,params=params)
        result.raise_for_status()
        print(result.json()["best_flights"][0])

        # print(self.departure,self.arrival,self.output_date,self.return_date)

fligth_google("MGA","CDG",)
