# Imports

from decouple import config

import requests

# Data Sources
SHEETY_USER_URL = config('SHEETY_FLIGHT_USER_URL')
SHEETY_API_KEY = config('SHEETY_KEY_FLIGHTDEALS')
header = {
    "Authorization": SHEETY_API_KEY,
}



class Customer:
    def __init__(self, cust_fname, cust_lname, cust_email):
        self.c_fname = cust_fname
        self.c_lname = cust_lname
        self.c_email = cust_email
        self.update_sheet()
    def update_sheet(self):
        print("Adding user to sheet!")
        parameters = {
            "user": [
                {
                    "firstName": self.c_fname,
                    "lastName": self.c_lname,
                    "email": self.c_email
                }
            ]
        }
        print(parameters)
        user_post = requests.post(url=SHEETY_USER_URL, headers=header, json=parameters)
        user_post.raise_for_status()
        print(user_post.json())

def gather_info():
    add_customer = True
    while add_customer:
        cust_data = input("Welcome to the Flight Club! Enter 'quit' to quit or Enter to proceed")
        if cust_data == "quit".lower():
            add_customer = False
        else:
            cust_fname = input("Please input first name:\n")
            cust_lname = input("Please input last name:\n")
            collect_email = True
            while collect_email:
                cust_email = input("Please input email address:\n")
                cust_emailverify = input("Please re-enter email address to verify:\n")
                if cust_emailverify == cust_email:
                    print("Thanks! Adding you to the Flight Club!")
                    customer = Customer(cust_fname, cust_lname, cust_email)
                    collect_email = False
                else:
                    print("The email address does not match. Please try again!")
