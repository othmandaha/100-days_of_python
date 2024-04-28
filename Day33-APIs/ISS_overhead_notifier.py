import requests
import datetime as dt
from math import isclose
import smtplib
    
LATITUDE = 35.731559
LONGITUDE = -5.806252
MY_EMAIL = ''
MY_PASSWORD = ''

#!----------------------- Is it Dark? --------------------------!#
def convetTo24(time):
    """formats time to 24 fomats"""
    if time[1] == 'PM':
        hour = time[0].split(':')
        hour = int(hour[0]) + 12
        return(hour)
    else:
        hour = time[0].split(':')
        hour = int(hour[0])
        return(hour)

def isDark():
    param = {
        'lat': LATITUDE, 
        'lng': LONGITUDE,
        'formatted': 1
    }

    currentTime = dt.datetime.now()
    currentTime = currentTime.hour

    respons = requests.get("https://api.sunrisesunset.io/json", param)
    respons.raise_for_status()
    respons = respons.json()
    sunrise = convetTo24(respons['results']['sunrise'].split(' '))
    sunset = convetTo24(respons['results']['sunset'].split(' '))

    if currentTime >= sunset or currentTime <= sunrise:
        return True
    else:
        return False

#!------------------- is ISS close? ------------------!#
def isISSclose():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])    

    if isclose(LATITUDE, iss_latitude, abs_tol=1) and isclose(LONGITUDE, iss_longitude):
        return True
    else:
        return False


#!------------------- send notification ------------------!#
while True:
    time.sleep(60)
    if isISSclose() and isDark():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )