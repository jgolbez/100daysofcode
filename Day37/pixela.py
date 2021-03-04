# Imports

# Requests - Send API Calls
import requests

# Decouple - Import ENV Variables
from decouple import config

# Date/Time Module
from datetime import datetime


# Data Sources / Global Variables

now = datetime.now()
print(now.strftime('%Y%m%d'))
pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = config('PIXELA_TOKEN')
pixela_username = "robertobobsono"
pixela_graphid = "graph666"

header = {
    "X-USER-TOKEN": pixela_token,
}

user_parameters = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsofService": "yes",
    "notMinor": "yes",
}

graph_parameters = {
    "id": pixela_graphid,
    "name": "Python Practice",
    "unit": "Day",
    "type": "int",
    "color": "shibafu",
}

pixel_parameters = {
    "date": "20200301",#now.strftime('%Y%m%d'),
    "quantity": "1",

}

put_parameters = {
    "quantity": "10",
}


# Main Loop

'''
#Create a User on Pixela

response = requests.post(url=pixela_endpoint, json=user_parameters)

# Create a new Pixel Graph

response_graph = requests.post(url=f"{pixela_endpoint}/{pixela_username}/graphs", json=graph_parameters, headers=header)

# Add Pixel to Graph

response_pixel = requests.post(url=f"{pixela_endpoint}/{pixela_username}/graphs/{pixela_graphid}", json=pixel_parameters, headers=header)


# Fix Bad Pixel Data

response_pixel = requests.put(url=f"{pixela_endpoint}/{pixela_username}/graphs/{pixela_graphid}/20200301", json=put_parameters, headers=header)

# Delete a Mistake Pixel

response_pixel = requests.delete(url=f"{pixela_endpoint}/{pixela_username}/graphs/{pixela_graphid}/20200301", headers=header)
'''