import json
from urllib.parse import urlencode
from urllib.request import urlopen

API_KEY = "6e7571a095ed78bb8e406610037e6759" # your API KEY
OPEN_WEATHERMAP_URL = "https://api.openweathermap.org/data/2.5/weather?"

city = input("City: ")

params = {'q': city, 'units': 'metric', 'appid': API_KEY}

url = OPEN_WEATHERMAP_URL + urlencode(params)

response = urlopen(url).read().decode()
data = json.loads(response)

weather_type = data['weather'][0]['main']
temp = data['main']['temp']

print(f"WEATHER IN {city.upper()}")
print("Outside is", weather_type, "and tempature is", temp)