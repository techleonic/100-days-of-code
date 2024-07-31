from smtplib import SMTP

import requests
from datetime import datetime
import smtplib
import requests

MY_LAT = 12.629960
MY_LONG = -87.127892

def is_iss_overhead():
    content = requests.get(url="http://api.open-notify.org/iss-now.json")
    content.raise_for_status()

    data = content.json()
    longitude = float( data["iss_position"]["longitude"])
    latitude = float(["iss_position"]["latitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {"lat":MY_LAT,"lng":MY_LONG,"formatted":0}

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now =  datetime.now().hour
    print(sunrise,sunset,time_now)
    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login("Email","password")
    connection.sendmail(from_addr="",to_addrs="",msg="Subject:look up\n\nThe iss is above you in the sky")


