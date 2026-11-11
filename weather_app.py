import requests

API_KEY = "62b66090cd0e38585a03e3cd7c12bd1c"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:

        data = response.json()

        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        fahrenheit = (temperature * 9/5) + 32

        print("\n----- WEATHER REPORT -----")
        print("City:", city_name)
        print("Temperature:", temperature, "°C")
        print("Temperature:", round(fahrenheit, 2), "°F")
        print("Humidity:", humidity, "%")
        print("Weather:", description)
        print("Wind Speed:", wind_speed, "m/s")

    else:
       print("Error Code:", response.status_code)
       print("Error Message:", response.text)

except requests.exceptions.RequestException:
    print("Network error! Please check your internet connection.")
