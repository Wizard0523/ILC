import requests
import json

API_URL = "api.openweathermap.org/data/2.5/weather?lat="
API_URL = "http://" + API_URL
KEY = "4bc8eb78acd942d6594974295c615f5f"

#coordinates for Olympia, WA
latitude = "47.0379"
longitude = "122.9007"

#final url (end point)
url = API_URL + latitude + "&lon=" + longitude + "&appid=" + KEY

response = requests.get(url).json()
#parse json
weather = response['weather'][0]['main']

print(weather)

