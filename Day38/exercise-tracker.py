# Imports

# Decouple - Pull hidden environment variables
from decouple import config

# Requests - Make API Calls
import requests

# Time
from datetime import datetime

# Data Sources/Global Variables

today = datetime.today()
date = today.strftime("%m/%d/%Y")
time = today.strftime("%H:%M:%S")
gender = "male"
weight_kg = 76.2
height_cm = 170.18
age = 40

# Nutritionix Data/Variables
nutritionix_api_key = config('NUTRITIONIX_API_KEY')
nutritionix_appid = config('NUTITIONIX_APP_ID')
nutritionix_api_url = "https://trackapi.nutritionix.com/v2/"
exercise_api = "natural/exercise"

n_header = {
    "x-app-id": nutritionix_appid,
    "x-app-key": nutritionix_api_key,
    "x-remote-user-id": "0",
}

# Sheety Data/Variables

### --- Example GET Response to Grab Data ---###
'''
sample URL: https://api.sheety.co/abc123random/workouts/workouts 
where workouts is name of project and workouts is name of sheet

{
    "workouts": [
        {
            "date": "21/07/2020",
            "time": "15:00:00",
            "exercise": "Running",
            "duration": 22,
            "calories": 130,
            "id": 2
        }
    ]
}
'''

### --- Example POST Body to Add Data ---###
'''
URL is same, but to POST, the root property "workout" below is required. If the sheet is named emails, property
will be "email"

{
    "workout": {
            "date": "05/03/2021",
            "time": "15:03:00",
            "exercise": "Biking",
            "duration": 53,
            "calories": 463
        }
}
'''

sheety_key = config('SHEETY_KEY')
sheety_url = config('SHEETY_TEST_URL')


s_header = {
    "Authorization": sheety_key,
}


###--- Functions ---###

# Parse exercise data returned by Nutritionix, make API Call to update sheet based on user submitted exercises
def create_exercise_params(ex_dict) -> dict:
    time_param = time
    #DEBUG:print(time_param)
    date_param = date
    #DEBUG:print(date_param)
    for index in ex_dict['exercises']:
        ex_name = index['name']
        #DEBUG:print(ex_name)
        ex_cal = index['nf_calories']
        #DEBUG:(ex_cal)
        ex_dur = index['duration_min']
        #DEBUG:print(ex_dur)
        submit_exercise_sheet(date_param, time_param, ex_name, ex_dur, ex_cal)

def submit_exercise_sheet(date_data, time_data, exercise_data, duration_data, calories_data):
    s_params = {
        "workout": {
            "date": date_data,
            "time": time_data,
            "exercise": exercise_data,
            "duration": duration_data,
            "calories": calories_data,
        }
    }
    sheety_post = requests.post(url=sheety_url, json=s_params, headers=s_header)
    sheety_post.raise_for_status()
#DEBUG:print(sheety_post)




# Main Loop
exercise_search_text = input("What exercise did you do today?")
exercise_search_json = {
    "query": exercise_search_text,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age,
}
exercise_response = requests.post(url=f"{nutritionix_api_url}{exercise_api}", headers=n_header, json=exercise_search_json)
exercise_response.raise_for_status()
exercise_dict = exercise_response.json()
#DEBUG: print(exercise_dict)
create_exercise_params(exercise_dict)
