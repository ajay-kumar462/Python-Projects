import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "#token"
USERNAME = "#user"
GRAPH_ID = "#graph"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
TODAY_FORMATTED = today.strftime("%Y%m%d")
pixel_input_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# print(today.strftime("%Y%m%d"))
pixel_input_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?: "),
}

response = requests.post(url=pixel_input_endpoint, json=pixel_input_config, headers=headers)
print(response.text)

pixel_input_endpoint_for_put = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_FORMATTED}"

pixel_input_config_new = {
    "quantity": "4"
}

# response = requests.put(url=pixel_input_endpoint_for_put, json=pixel_input_config, headers=headers)
# print(response.text)

pixel_input_endpoint_for_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_FORMATTED}"

# response = requests.delete(url=pixel_input_endpoint_for_delete, headers=headers)
# print(response.text)

