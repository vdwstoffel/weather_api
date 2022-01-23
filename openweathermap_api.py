import requests
from datetime import datetime


class OpenWeatherMap:
    def weather_data(self, owm_api):
        """API Call the get the weather data from OpenWeatherMap.org"""
        weather_parameters = {
            "lat": "51.0543",
            "lon": "3.7174",
            "appid": owm_api,
            "exclude": ["minutley", "daily"],
            "units": "metric"
        }
        response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                                params=weather_parameters)
        response.raise_for_status()
        return response.json()

    def rain(self, data):
        """Get the next 24h rain information and check for how many hours it will rain."""
        hourly = data["hourly"]
        return sum(hour['weather'][0]["id"] < 800 for hour in hourly[0:24])


    def temperature(self, data):
        """Get the average temperature for the day"""
        return data["current"]["temp"]

    def daily_sun(self, data):
        # times in UNIX datetime
        sunrise = data["current"]["sunrise"]
        sunset = data["current"]["sunset"]

        sun_hours = sunset - sunrise
        # Convert Unix to float/Pixela does not supprot datetime so float will be used ie. 07:54 = 07.54
        return datetime.utcfromtimestamp(sun_hours).strftime("%H.%M")

    def sunrise_sunset(self, data):
        """Get the sunrise and sunset"""
        # times in UNIX datetime, converted to normal time
        sunrise = datetime.fromtimestamp(data["current"]["sunrise"])
        sunset = datetime.fromtimestamp(data["current"]["sunset"])

        return sunrise.strftime("%H:%M:%S"), sunset.strftime("%H:%M:%S")
