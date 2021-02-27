

#https://api.sunrise-sunset.org/json
# Imports
import requests
from datetime import datetime

#Data Sources/Global Variables
parameters = {
    "lat": 35.95907,
    "lng": -78.54366,
    "formatted": 0
}
sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()['results']
sunrise_hour = int(sun_data['sunrise'].split("T")[1].split(":")[0])
sunset_hour = int(sun_data['sunset'].split("T")[1].split(":")[0])

sunrise_est = sunrise_hour - 5
sunset_est = sunset_hour - 5
now = datetime.now()
now_hour = int(now.hour)

