import requests

APP_ID = "#apiid"
API_KEY = "#apikey"

exercise_endpoint = "https://api.api-ninjas.com/v1/caloriesburned"

user_params = {
    "activity": input("What was your exercise today?: ")
}
headers = {
    "X-Api-Key": API_KEY,
}

response = requests.get(url=exercise_endpoint, params=user_params, headers=headers)
# print(response.json())

sheets_endpoint = "https://api.sheety.co/245205278abf1d72e76ae2210b1ea2f5/myWorkouts/workouts"

sheets_config_json = {
    "workout": {
        "Date": "3/11/2025",
        "Time": "15:00:00",
        "Exercise": response.json()[0]["name"],
        "Duration": response.json()[0]["duration_minutes"],
        "Calories": response.json()[0]["total_calories"],
    }
}
sheet_response = requests.post(url=sheets_endpoint, json=sheets_config_json)
print(sheet_response.json())
