import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

response_data = response.json()["iss_position"]
print(response_data)

iss_pos = (response_data["latitude"], response_data["longitude"])
print(iss_pos)