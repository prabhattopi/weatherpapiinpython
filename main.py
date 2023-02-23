# importing the required libraries
import requests

# ENTER THE the api key of openweahtermap

api_key = input("Enter your Api key: ")

# Base url for the open map api

root_url = "http://api.openweathermap.org/data/2.5/weather?"

# city name

city_name = input("What city do you want to know weather? ")

# butilding the final url for the Api call

url = f"{root_url}appid={api_key}&q={city_name}"

# sending the request at the url

r = requests.get(url)

# display the json weather data

print(r.json())

# store the json data into a variable

data = r.json()

# checking if threre is no error

if data["cod"] == 200:
    # getting the required information
    temp = data["main"]["temp"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    decr = data["weather"][0]["description"]
    wind = data["wind"]["speed"]

    print(f"city name: {city_name}")
    print(f"description of {city_name} is {decr}")
    print(f"tempreature of {city_name} is {temp} Kelvin")
    print(f"pressure of {city_name} is {pressure} hpa")
    print(f"humidity of {city_name} is {humidity}%")

    print(f"wind speed of {city_name} is {wind}m/s")

else:
    print("something went wrong please put diffrent or correct city name")
