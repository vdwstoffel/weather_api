from login_details import Login
from openweathermap_api import OpenWeatherMap
from pixela_api import Pixela
from database_data import Database
from email_manager import Email
from datetime import datetime

login = Login("credentials.json")
owm = OpenWeatherMap()
pixela = Pixela()
db = Database("weather.sqlite", "weather_data")
stoffel = Email("vdwstoffel@gmail.com")
today = datetime.now().strftime("%Y%m%d")
formatted_date = f"{today[0:4]}/{today[4:6]}/{today[6:]}"

# Create database
db.create_database()
db.create_table()

# Load the credentials for openweathermap and pixela
credentials = login.get_credentials()
if credentials:
    # Get the data from open weather map
    weather_data = owm.weather_data(credentials[0])

    # Create the different datasets
    rain = owm.rain(weather_data)
    temp = owm.temperature(weather_data)
    sun = owm.daily_sun(weather_data)
    sun_times = owm.sunrise_sunset(weather_data)

    # Save data to database
    db.record_data(formatted_date, rain, temp, sun, sun_times[0], sun_times[1])

    # Post data to pixela
    pixela.post(credentials[1], credentials[2], rain, temp, sun, today)

    # send email to user
    stoffel.send_email(credentials[3], credentials[4],
                       formatted_date, sun_times[0], sun_times[1], temp, rain)
