import json

import requests

# Ex 12.1
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print("Random Chuck Norris joke:")
print(response["value"])

# Ex 12.2
city = input("Enter city: ")
city = city.capitalize()
key = "########################"
request = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key + "&units=metric"
response = requests.get(request).json()
weather = response["weather"][0]["description"]
temp = response["main"]["temp"]
print(f"Current weather at {city}: {weather}\nTemperature: {temp}")