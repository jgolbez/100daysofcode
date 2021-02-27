#Imports
import requests
from datetime import datetime
import time
import smtplib


#Data Sources/Global Variables

my_email = "robertobobsono@gmail.com"
email_pw = "nice_try_no"

MY_LAT = 28.38533 # Your latitude
MY_LONG = -81.56384 # Your longitude

time_now = datetime.now()
now_hour = int(time_now.hour)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
#Functions

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"Current ISS Lat: {iss_latitude}")
    print(f"Current ISS Lat: {iss_longitude}")
    LAT_OK = MY_LAT-5 <= iss_latitude <= MY_LAT+5
    LONG_OK = MY_LONG-5 <= iss_longitude <= MY_LONG+5
    return LAT_OK and LONG_OK

def dark_sky():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_est = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
    sunset_est = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 5
    print(f"Sunrise: {sunrise_est}")
    print(f"Sunset: {sunset_est}")
    print(f"Time: {now_hour}")
    return now_hour > sunset_est or now_hour < sunrise_est

def check_iss_visible():
    visible = dark_sky()
    print(f"Dark Sky: {visible}")
    overhead = iss_overhead()
    print(f"ISS Overhead: {overhead}")
    return visible and overhead

#Main Loop

while True:
    send_email = check_iss_visible()
    if send_email:
        print(f"Send Email: {send_email}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_pw)
            connection.sendmail(
            from_addr=my_email,
            to_addrs="someone@gmail.com",
            msg="Subject:ISS Now Visible Overhead\n\nAlert! The ISS is now visible in the night sky overhead!"
        )
    print("Sleeping for 60 seconds")
    time.sleep(60)
