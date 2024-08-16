import  os
from datetime import datetime
import requests
from flask import jsonify
GENDER = "MALE"
WEIGHT_KG = 72
HEIGHT_CM = 180
AGE = 27

APP_ID = os.environ.get("NUTRIONIX_ID")
API_KEY = os.environ.get("NUTRIONIX_APIKEY")

print(APP_ID, API_KEY)

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
########################## INSERT ROW #######################
SHEETY_ENDPOINT =  os.environ.get("SHEETY_ENDPOINT")
date_now = datetime.now().strftime("%d/%m/%Y")
hour = datetime.now().strftime("%X")

authorization = os.environ.get("Authorization")
headers = {
    "Authorization":authorization
}

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout":{
            "date":date_now,
            "time": hour,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    print(sheety_parameters, headers)
    sheety_response =  requests.post(url=SHEETY_ENDPOINT,json=sheety_parameters,headers=headers)
    sheety_response.raise_for_status()
    print(sheety_response.text)

# ##### FILTER ROW WITH A QUERY #####
# today_date = datetime.now().strftime("%d/%m/%Y")
# hour = datetime.now().strftime("%X")
# query = {
#     "filter":{
#         "Exercise":"Running"
#     }
# }
#
# sheety_response = requests.get(url=SHEETY_ENDPOINT,json=query)
# sheety_response.raise_for_status()
#
# print(sheety_response.links)
# print(sheety_response.text)
