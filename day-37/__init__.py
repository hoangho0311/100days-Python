import requests
from datetime import datetime

pixela_end = "https://pixe.la/v1/users"
token = "1234567cu2"
username = "hoangho"
paramater = {
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# respone = requests.post(url=pixela_end, json=paramater)
graphid = "graph1"
graph_endpoint = f"{pixela_end}/{username}/graphs"
graph_params = {
    "id":graphid,
    "name":"Graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji",
}
headres={
    "X-USER-TOKEN":token
}
# graph_respone = requests.post(url=graph_endpoint, json=graph_params, headers=headres)
# print(graph_respone.text)

post_endpoint = f"{pixela_end}/{username}/graphs/{graphid}"
post_params = {
    "date":datetime.strftime("%Y%m%d"),
    "quantity": "9.74",
}

# post_respone = requests.post(url=post_endpoint, json=post_params, headers=headres)
# print(post_respone.text)




