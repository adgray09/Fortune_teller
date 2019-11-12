import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

weather_url = "http://api.openweathermap.org/data/2.5/weather?q=Louisville&appid=2608f679d4594364525f6c6cc2246c79"

response = requests.get(weather_url)
response_json = response.json()

main_data = response_json["main"]
temp_in_kelvin = main_data["temp"]
print(" it is now " + str(temp_in_kelvin) + " degrees kelvin.")