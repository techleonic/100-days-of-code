import requests
from datetime import datetime

date = datetime.strftime(datetime.now(),"%Y%m%d")


pixela_endpoint = "https://pixe.la/v1/users"
username = "leotechnic27"
graph = "graph1"

graph_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph}/{date}"
print(graph_endpoint)
params = {
    "quantity":"10"
}

headers = {
    "X-USER-TOKEN":"ijljhljhjljhljghfyfdy456"
}
# update
# response = requests.put(url=graph_endpoint,json=params,headers=headers)
# delete
response = requests.delete(url=graph_endpoint,headers=headers)
print(response.text)



