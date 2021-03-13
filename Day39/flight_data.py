# FlightData class is used to create a per-flight object with details about the flight to compare to lowest price
# and provide the needed attributes for text messaging
class FlightData:
    def __init__(self, f_fare, f_arr_city, f_arr_code, f_dep_date, f_ret_date):
        self.f_fare = f_fare
        self.f_dep_city = "Raleigh"
        self.f_dep_code = "RDU"
        self.f_arr_city = f_arr_city
        self.f_arr_code = f_arr_code
        self.f_dep_date = f_dep_date
        self.f_ret_date = f_ret_date