# wpisz w konsoli w folderze example: python weather2 Warsaw

import requests
import sys
from collections import namedtuple

# z namedtuple mozna to jeszcze inaczej zrobic, patrz kod prowadzacego na github
# mozna tez stworzyc class weather

localization = sys.argv[1]
# localization = "Warsaw"

def get_location_id(localization):
    """pobieram id lokalizacji """
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={localization}")
    location_id = resp.json()[0]['woeid']
    return location_id


def get_location_weather(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    wheater = resp.json()['consolidated_weather'][0]
    return wheater


# drukuje info o pogodzie
def print_weather(weather, localization):
    print(f"Pogoda w lokalizacji: {localization}")
    print(f"Temperatura: {weather['the_temp']}")
    print(f"Ciśnienie_powietrza: {weather['air_pressure']}")
    print(f"Wilgotność powietrza: {weather['humidity']}")


location_id = get_location_id(localization)
weather = get_location_weather(location_id)
print_weather(weather, localization)
input("wcisnij dowolny klawisz")
