import requests
from datetime import datetime
import os
AGE = 21
WEIGHT = 58
HEIGHT = 179


#* APIS Endpoints and Keys
NUTRITIONX_ID = os.environ.get("NUTRITION_ID")   # get nutritionx id from here https://www.nutritionix.com/business/api
NUTRITIONX_API_KEY = os.environ.get("NUTRITION_API_KEY")  # get nutritionx key from here https://www.nutritionix.com/business/api
X_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT") # get the endpoint to your sheet from here https://sheety.co/



#* Generate and parses todays date and time
dt = datetime.now()
date = dt.date()
date = date.strftime("%d/%m/%Y")
time = dt.time()
time = time.strftime("%H:%M:%S")

print(date)
print(time)

#* https header authentifiaction
headers = {
    "x-app-id": NUTRITIONX_ID,
    "X-app-key": NUTRITIONX_API_KEY
}


#* user input
query = input("Tell me which exercises you did: ")


#* nutritionx parameters
para = {
    "query": query,
    "age": AGE,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT
}

#* retrieving and parsing the result nutristion x
respons = requests.post(url=X_ENDPOINT, json=para, headers=headers)
respons.raise_for_status()
result = respons.json()

exerciseName = result['exercises'][0]['name']
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']


#* POSTING THE RESULTS TO SHEETY
row_content = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exerciseName.title(),
        "duration": duration,
        "calories": calories
    }
}

sheetyRespons = requests.post(url=SHEETY_ENDPOINT, json=row_content)
sheetyRespons.raise_for_status()
print(sheetyRespons.text)


