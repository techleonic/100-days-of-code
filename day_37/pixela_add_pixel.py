import requests
from datetime import datetime


date = datetime.strftime(datetime.now(),"%Y%m%d")
print(date)

pixela_endpoint = "https://pixe.la/v1/users"
username = "leotechnic27"
graph = "graph1"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph}"

params = {
    "date":str(date),
    "quantity":"5"
}

headers = {
    "X-USER-TOKEN":"ijljhljhjljhljghfyfdy456"
}
response = requests.post(url=graph_endpoint,json=params,headers=headers)
print(response.text)