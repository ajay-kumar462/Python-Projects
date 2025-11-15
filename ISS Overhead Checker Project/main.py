import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = 47.01#float(data["iss_position"]["latitude"])
iss_longitude = -1.21#float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def in_position():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
    if time_now.hour > sunset and time_now.hour < sunrise:
        return True

while True:
    time.sleep(60)
    if in_position() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="ajaytestacc12@gmail.com", password="bmfgnlxbsctrpqoy")
            connection.sendmail(from_addr="ajaytestacc12@gmail.com", to_addrs="ajaytestacc12@gmail.com", msg="Subject: Look up at the sky!\n\nThe ISS is overhead.")
        print("mail sent")
