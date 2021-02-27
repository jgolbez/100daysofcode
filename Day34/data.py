# Imports

import requests

# Data Sources/Global Variables

parameters = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()['results']
print(question_data)
