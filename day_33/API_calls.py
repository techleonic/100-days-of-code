import requests

content = requests.get(url="http://api.open-notify.org/iss-now.json")
content.raise_for_status()

data = content.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(data)
