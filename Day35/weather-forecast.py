# Imports
import requests
from decouple import config
from twilio.rest import Client

# Data Sources/Global Variables

# Data Source - OpenWeather API
weather_api = "https://api.openweathermap.org/data/2.5/"
OPENWEATHER_API_KEY = config("OPENWEATHER_API_KEY")
lat = config('TEST_LAT')
lon = config('TEST_LONG')

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": OPENWEATHER_API_KEY,
    "exclude": "current,minutely,daily,alerts",
}
weather_response = requests.get(f"{weather_api}/onecall", params=parameters)
weather_response.raise_for_status()
#Slice the index of the dict so it returns only 0-12
hourly_weather = weather_response.json()['hourly'][:12]

# Data Source - Twilio API
account_sid = config('TWILIO_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
twilio_phone = config('TWILIO_PHONE_NUMBER')
test_phone = config('TEST_PHONE_NUMBER')

# Main Loop - Will It Rain - OpenWeather API

will_rain = False
# Use For Loop to iterate through dict by hour
for w_id in hourly_weather:
    if w_id["weather"][0]["id"] < 700:
        print(f"Code: {w_id['weather'][0]['id']}")
        will_rain = True
if will_rain:
# Main Loop - Twilio SMS App API
    message = client.messages \
                .create(
                     body="IT'S GON' RAIN!",
                     from_=f"+{twilio_phone}",
                     to=f"+{test_phone}"
                 )
    print(message.status)
