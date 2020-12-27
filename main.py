import requests
from datetime import datetime

PIXELA_USERNAME = "arjun"
PIXELA_API_NEW_USER_URL = "https://pixe.la/v1/users/"
PIXELA_API_NEW_GRAPH_URL = "https://pixe.la/v1/users/" + PIXELA_USERNAME + "/graphs"
PIXELA_API_GRAPH_URL = "https://pixe.la/v1/users/" + PIXELA_USERNAME + "/graphs/pythongraph"
PIXELA_TOKEN = "arjun234"

pixela_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": "pythongraph",
    "name": "Learning Python",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

today = datetime(year=2020, month=12, day=26)
print(today.strftime("%Y%m%d"))

pixel_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "100"
}

PIXELA_API_GRAPH_DAY_URL = PIXELA_API_GRAPH_URL + "/" + today.strftime("%Y%m%d")

#pixela_data = requests.post(url=PIXELA_API_NEW_USER_URL, json=pixela_params)
#pixela_data = requests.post(url=PIXELA_API_NEW_GRAPH_URL, json=graph_config, headers=headers)
#pixela_response = requests.post(url=PIXELA_API_GRAPH_URL, json=pixel_update, headers=headers)
#pixela_response = requests.put(url=PIXELA_API_GRAPH_DAY_URL, json=pixel_update, headers=headers)
pixela_response = requests.delete(url=PIXELA_API_GRAPH_DAY_URL, headers=headers)

#print(pixela_data.json())
print(pixela_response.json())
