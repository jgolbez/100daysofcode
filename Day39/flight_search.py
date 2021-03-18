# Imports

# Access the FlightData class/attribs/methods
from flight_data import FlightData

# Import hidden environ variables
from decouple import config

# Make API Calls
import requests

# Do time-based functions
from datetime import datetime, timedelta

# Data Sources/Global variables

now = datetime.now()
current_time = now.strftime("%d/%m/%Y")
fly_from_date = (now + timedelta(days=1)).strftime("%d/%m/%Y")
fly_to_date = (now + timedelta(days=(6*30))).strftime("%d/%m/%Y")
print(f"Search for flights leaving between {fly_from_date} and {fly_to_date}")
length_stay_min = 7
length_stay_max = 28

TEQUILA_API_URL = "https://tequila-api.kiwi.com/"
TEQUILA_API_LOC_SEARCH = "locations/query"
TEQUILA_API_KEY = config('FLIGHT_SEARCH_API_KEY')

headers = {
    "apikey": TEQUILA_API_KEY,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_url = TEQUILA_API_URL
        self.api_headers = headers

    # If the city code is missing from Google sheets, pull in a list of the city names from DataManager to run a query,
    # return dict of city / code for Sheet updates
    def loc_query(self, loc_list) -> list:
        self.city_code = {}
        self.city_code_list = []
        for city in loc_list:
            #DEBUG print(city)
            self.parameters = {
                "term": city
            }
            response = requests.get(url=f"{TEQUILA_API_URL}{TEQUILA_API_LOC_SEARCH}", headers=self.api_headers,
                                    params=self.parameters)
            response.raise_for_status()
            #DEBUG print(response.json())
            self.city_code['city'] = response.json()['locations'][0]['name']
            self.city_code['code'] = response.json()['locations'][0]['code']
            #DEBUG print(self.city_code)
            #DEBUG print("Appending to list...")
            self.city_code_list.append(self.city_code.copy())
        return self.city_code_list

    # Pull in flight search variables
    def flight_search(self, city_code):
        parameters = {
            "fly_from": "RDU",
            "fly_to": city_code,
            "date_from": fly_from_date,
            "date_to": fly_to_date,
            "nights_in_dst_from": length_stay_min,
            "nights_in_dst_to": length_stay_max,
            "curr": "USD",
            "adults": 4,
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        print(f"Now searching for flights to {city_code}")
        f_search = requests.get(url=f"{self.api_url}v2/search", params=parameters, headers=self.api_headers)
        f_search.raise_for_status()
        print(f_search.json())
        try:
            f_dict = f_search.json()['data'][0]
        except IndexError:
            parameters['max_stopovers'] = 2
            f_search = requests.get(url=f"{self.api_url}v2/search", params=parameters, headers=self.api_headers)
            f_search.raise_for_status()
            print(f" Rerunning with up to 2 max stopovers\n {f_search.json()}")
            try:
                f_dict = f_search.json()['data'][0]
            except IndexError:
                print("No flights are available")
                return None
            f_fare = f_dict['price']
            f_dep_city = "Raleigh"
            f_dep_code = "RDU"
            f_arr_city = f_dict['cityTo']
            f_arr_code = city_code
            f_dep_date = f_dict['route'][0]['local_departure'].split('T')[0]
            f_ret_date = f_dict['route'][1]['local_departure'].split('T')[0]
            f_stop_over = 1
            f_via_city = f_dict['route'][0]['cityTo']
            flight = FlightData(f_fare, f_arr_city, f_arr_code, f_dep_date, f_ret_date, f_stop_over, f_via_city)
            return flight
        else:
            f_fare = f_dict['price']
            f_dep_city = "Raleigh"
            f_dep_code = "RDU"
            f_arr_city = f_dict['cityTo']
            f_arr_code = city_code
            f_dep_date = f_dict['route'][0]['local_departure'].split('T')[0]
            f_ret_date = f_dict['route'][1]['local_departure'].split('T')[0]
            flight = FlightData(f_fare, f_arr_city, f_arr_code, f_dep_date, f_ret_date)
            print(f"Fare:{f_fare}")
            print(f"Departure City:{f_dep_city}")
            print(f"Departure Code:{f_dep_code}")
            print(f"Arrival City:{f_arr_city}")
            print(f"Arrival Code:{f_arr_code}")
            print(f"Departure Date:{f_dep_date}")
            print(f"Return Date:{f_ret_date}")
            return flight










