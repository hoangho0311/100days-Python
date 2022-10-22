import requests
from  datetime import datetime

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 170
AGE = 18

APP_ID = "a95e5c5e"
API_KEY = "b8a78678609fb95a81b4563885688fa8"

sheet_endpoint = "https://api.sheety.co/8a547f217503367df6a68105dfe6ace6/workout/trangTính1"
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
result = response.json()

today = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs={
        "trangTính1":{
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

print(sheet_response.text)