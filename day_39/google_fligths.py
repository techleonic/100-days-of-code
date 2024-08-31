import json

import requests
import os
from datetime import datetime,timedelta

class fligth_google():
    """retruns a json with all the flights"""
    def __init__(self,departure,arrival,output_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
    return_date = (datetime.now() + timedelta(days=8)).strftime("%Y-%m-%d")):
        self.departure = departure
        self.arrival = arrival
        self.output_date = output_date
        self.return_date = return_date
        self.end_point = "https://serpapi.com/search?engine=google_flights"
    def get_flights(self):
        params = {"engine":"google_flights",
                  "api_key": os.getenv("SerApi"),
                  "departure_id":self.departure,"arrival_id":self.arrival,
                  "outbound_date":self.output_date,"return_date":self.return_date}
        # print(params)
        result = requests.get(url=self.end_point,params=params)
        data = result.json()
        json_object =  json.dumps(data,indent=4)
        with open("maindata.json","w") as file:
            file.write(json_object)

        return data

        # print(self.departure,self.arrival,self.output_date,self.return_date)


