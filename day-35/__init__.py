import requests

hoang_api = "210327fc7a976a66bd2097dc446dc57f"

request = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={hoang_api}")
data = request.raise_for_status()

print()