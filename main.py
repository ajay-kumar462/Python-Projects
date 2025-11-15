import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "#myapikey"

account_sid = "#myaccountsid"
auth_token = "#myauthtoken"

parameters = {
    "lat": 40.511036, #19.075983
    "lon": 141.490410, #72.877655
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_id = response.json()["list"][0]["weather"][0]["id"]

print(weather_data)
print(weather_id)
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
    else:
        print("No umbrella needed")

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG972d79b8ed1e95a3f1396433c20cfae6',
        body="It's going to rain today. Remember to bring an ☂️.",
        from_="+14066268198",
        to="+919930340173",
    )
    print(message.status)