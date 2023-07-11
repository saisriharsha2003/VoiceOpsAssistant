import requests


def get_temperature(api_key, city):
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
        return temperature
    else:
        print("Error retrieving temperature data.")
        print("Response:", weather_data)
        return None


# Replace 'YOUR_API_KEY' with the API key you obtained from OpenWeatherMap
api_key = "846900d09922d876b13e3ded54c99d46"
# Replace 'YOUR_CITY' with the name of your city
city = "Delhi"

temperature = get_temperature(api_key, city)
if temperature is not None:
    print(f"The temperature in {city} is {temperature}°C.")
