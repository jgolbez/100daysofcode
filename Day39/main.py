# Imports

#Import classes
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from customer_info import gather_info, Customer

# Pull Google sheet data and build list of cities missing codes (if needed)
sheet = DataManager()
print(sheet.sheet_data)
blank_city_codes = [city['city'] for city in sheet.sheet_data if city['iataCode'] == '']
print(blank_city_codes)


# Access flight search methods
fsearch = FlightSearch()
# If some city codes are empty, start a query to Tequila API to return city codes  and update for later flight search
if len(blank_city_codes) > 0:
    city_codes = fsearch.loc_query(blank_city_codes)
    #DEBUG print(city_codes)
    sheet.update_sheet(city_codes)


# With full city code data, execute flight search for provided criteria and create FlightData object for each flight
# FlightData object is created under Flight_Search and is appended to an object list here
list_of_flights = []
for city in sheet.sheet_data:
    city_flight = fsearch.flight_search(city['iataCode'])
    list_of_flights.append(city_flight)


# Search through list of flight objects, per city, t see if fare is lower than Google sheet
# If so create NotificationManager object to feed in flight details, send text message before moving on to next flight
for city in sheet.sheet_data:
    for flight in list_of_flights:
        if city['iataCode'] == flight.f_arr_code:
            if int(city['lowestPrice']) > int(flight.f_fare):
                notify = NotificationManager()
                print(f"Found a hit! Notifying about {city['iataCode']}")
                notify.notify_sms(flight.f_fare, flight.f_dep_city, flight.f_dep_code, flight.f_arr_city,
                                             flight.f_arr_code, flight.f_dep_date, flight.f_ret_date,
                                  flight.f_stopovers, flight.f_via_city)



