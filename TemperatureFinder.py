import requests
from config import owmapikey
from virtual_assistant import speak,inputCommand, desktop_assistant, user

def get_temperature_of_city():
    print(desktop_assistant + ": For which location you need its temperature Sir?")
    speak("For which location you need its temperature Sir?")
    city = inputCommand()
    print(user + ": " + city)
    print(desktop_assistant + ": Sure Sir! Wait a While,let me check the temperature of given location.....")
    speak("Sure Sir! Wait a While,let me check the temperature of given location.....")
    api_key = owmapikey
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    if "main" in weather_data and "temp" in weather_data["main"]:
        temperature = weather_data["main"]["temp"]
        print(desktop_assistant + f": The temperature in {city} is {temperature}°C.")
        speak(f"The temperature in {city} is {temperature}°C.")
    else:
        print(desktop_assistant + ": Error retrieving temperature data.")
        speak("Error retrieving temperature data.")
        print(desktop_assistant + ": Response:", weather_data)
        speak("Response:" + weather_data)