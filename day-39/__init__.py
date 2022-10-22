import requests

parameters={

}

respone = requests.post(url="https://api.sheety.co/8a547f217503367df6a68105dfe6ace6/flightDeals/trangTính1")
print(respone.json())