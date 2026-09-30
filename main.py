# import requests
# api_key="93a6fd854517b81dfc6f34a168108d14"
# city=input("Enter city:")
# url=" f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
# params={
#         "q":city,
#         "apiid":api_key,
#         "units":"metric"
#         }
# response=requests.get(url,params=params)
# print(response.status_code)
# data=response.json()
# print(data)
import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("weather_api_key")
city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

print(response.status_code)
data=response.json()
print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Weather:", data["weather"][0]["description"])