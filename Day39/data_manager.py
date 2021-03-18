# Imports

# Decouple - Access hidden environment variables
from decouple import config

# Requests - Make API calls

import requests


# Class Definition - DataManager will handle all Sheety/Google Sheet Interactions
class DataManager:
    def __init__(self):
        self.apikey = config('SHEETY_KEY_FLIGHTDEALS')
        self.sheety_url = config('SHEETY_FLIGHT_URL')
        self.sheety_headers = {
            "Authorization": self.apikey,
        }
        self.sheet_data = self.get_sheet()

# Pull data from Google sheet to use for flight search
    def get_sheet(self):
        sheety_response = requests.get(url=self.sheety_url, headers=self.sheety_headers)
        sheety_response.raise_for_status()
        print(sheety_response.json())
        return sheety_response.json()['prices']
        #TESTING output below
        #return [{'city': 'Barcelona', 'iataCode': '', 'lowestPrice': 4000, 'id': 2},
        #            {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 500, 'id': 3},
        #            {'city': 'Taipei', 'iataCode': 'TPE', 'lowestPrice': 350, 'id': 4},
        #            {'city': 'Orlando', 'iataCode': 'MCO', 'lowestPrice': 350, 'id': 5}]

#If any cities lack an airport/city code, update the sheet with the airport/city code based on Tequila API search
#to avoid having to do it next time
    def update_sheet(self, city_codes) -> dict:
        #DEBUG print(self.sheet_data)
        #DEBUG print(city_codes)
        for city in self.sheet_data:
            for city_code in city_codes:
                if city_code['city'] == city['city']:
                    city_row_id = city['id']
                    city['iataCode'] = city_code['code']
                    city_iata = city_code['code']
                    #DEBUG print(city_row_id, city_iata)
                    update_url = f"{self.sheety_url}/{city_row_id}"
                    body = {
                        "price": {
                            "iataCode": city_iata
                        }
                    }
                    sheet_iata_add = requests.put(url=update_url, headers=self.sheety_headers, json=body)
                    sheet_iata_add.raise_for_status()
                    #DEBUG print(sheet_iata_add)
                    # TESTING output below
                    #DEBUG print(f"Code for {city_iata} updated successfully)")
