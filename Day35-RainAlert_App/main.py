import requests
import os
from twilio.rest import Client

MY_KEY = os.environ.get("OPEN_WEATHER_KEY")
LONGIUDE = 7.683070
LATITUDE = 45.068371
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")


#!------------------- Open_Weahter_API ------------------!#
para = {
    'lat': LATITUDE,
    'lon': LONGIUDE,
    'appid': MY_KEY,
    'exclude': "current,minutely,daily"
}
respons = requests.get('https://api.openweathermap.org/data/3.0/onecall', params=para)
respons.raise_for_status()
respons = respons.json()

#!--------------- Rain Checker Logic ---------------!#
first12h = respons['hourly'][:12]
def is_rainy():
    rainy = False
    for i in first12h:
        id = i['weather'][0]['id']
        if id < 700:
            rainy = True
            break
    return rainy

#!--------------- Twilio SMS sender Setup ------------------!#
if is_rainy():
    #Connect 
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        body="It's gonna rain, bring an umbrella ☔",
        from_='+14793163288',
        to='+21266348423'
    )
    print(message.status)

