import requests 


# using openweathermap api
api_key = "03d9b86ae11e33a003449755b9989735"
user_input = input("Enter city name: ")
weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.status_code != 200:
    print("City not found")
else:
    weather = weather_data.json()["weather"][0]["description"]
    temperature = weather_data.json()["main"]["temp"]
    print(f"Temperature: {temperature}°F\nWeather: {weather}")





