import requests
pixela_endpoint = "https://pixe.la/v1/users"
username = "leotechnic27"

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_params = {
    "id":"graph1",
    "name":"Exercising Graph",
    "unit":"commits",
    "type":"int",
    "color":"kuro",

}
headers= {
"X-USER-TOKEN":"ijljhljhjljhljghfyfdy456"
}

response =  requests.post(url=graph_endpoint,json=graph_params,headers=headers)
print(response.text)