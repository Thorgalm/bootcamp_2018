import requests
import sys

# ze strony https://www.metaweather.com/api/ uruchomic link do lokalizacji, gdzie w quary podajemy miasto, z tej strony wybieramy id miasta, wchodzimy na strone:
# https://www.metaweather.com/api/location/523920/ gdzie numer to id Warsaw
# i pobieramy dane o pogodzie

localization = sys.argv[1]
# localization = "Warsaw"

# pobieram id lokalizacji
resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={localization}")
location_id = resp.json()[0]['woeid']
# print(location_id)

resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
weather = resp.json()['consolidated_weather'][0]
# print(wheater)

#drukuje info o pogodzie
print(f"Pogoda w lokalizacji: {localization}")
print(f"Temperatura: {weather['the_temp']}")
print(f"Ciśnienie_powietrza: {weather['air_pressure']}")
print(f"Wilgotność powietrza: {weather['humidity']}")




# city_name = None
# if len(sys.argv) > 1:
#     city_name = sys.argv[1]
#
# if city_name:
#     with open(city_name) as f:
#         for i, line in enumerate(f, start=1):
#             print(f"{i}: {line}", end="")
# else:
#     print("Nie podałeś miasta")
#
# resp = requests.get("https://www.metaweather.com/api/location/search/?query="+city_name)
# print(resp)

# try:
#     with open(city) as city:
#         for
#
# except FileNotFoundError:
#     print("Nie ma takiego miasta")