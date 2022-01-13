from login_details import Login
from openweathermap_api import OpenWeatherMap
from pixela_api import Pixela
from database_data import Database
from datetime import datetime

login = Login("credentials.json")
owm = OpenWeatherMap()
pixela = Pixela()
db = Database("weather.sqlite", "weather_data")
today = datetime.now().strftime("%Y%m%d")

# Create database
db.create_database()
db.create_table()

# Load the credentials for openweathermap and pixela
credentials = login.get_credentials()

# Get the data from open weather map
weather_data = owm.weather_data(credentials[0])

# Create the different datasets
rain = owm.rain(weather_data)
temp = owm.temperature(weather_data)
sun = owm.daily_sun(weather_data)

# Save data to database
db.record_data(today, rain, temp, sun)

# Post data to pixela
pixela.post(credentials[1], credentials[2], rain, temp, sun, today)