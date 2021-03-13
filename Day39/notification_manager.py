# Imports

#Decouple - Access hidden environment variables
from decouple import config

#Twilio - Send SMS messages via REST API
from twilio.rest import Client

# Data Source - Twilio API
account_sid = config('TWILIO_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
twilio_phone = config('TWILIO_PHONE_NUMBER')
test_phone = config('TEST_PHONE_NUMBER')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(self.account_sid, self.auth_token)
        self.twilio_phone = twilio_phone
        self.test_phone = test_phone

    # If lower fare is available than entered in Google sheet for this city, pull in flight details and send text
    def notify_sms(self, n_fare, n_dep_city, n_dep_code, n_arr_city, n_arr_code, n_dep_date, n_ret_date):
        message = client.messages \
            .create(
            body=f"Low Price Alert! Only {n_fare} to fly from {n_dep_city}-{n_dep_code} to {n_arr_city}-{n_arr_code},"
                 f"from {n_dep_date} to {n_ret_date}.",
            from_=f"+{twilio_phone}",
            to=f"+{test_phone}"
        )


