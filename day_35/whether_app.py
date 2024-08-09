import requests

API_key = "1c9adbcb4a1623fd3d2f9ba8e9095b3b"
city_name = "San jose"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
data = response.json()
weather = data["weather"]
current_wether = weather[0]["main"]

if current_wether == "Rain":
    print("you need a umbrella")
else:
    print(f"dont need for umbrella cause we will have {current_wether} today")