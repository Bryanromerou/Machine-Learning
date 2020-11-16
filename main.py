import pandas as pd
import requests
from pprint import pprint

my_data = pd.read_csv("data.csv")
url = "https://realtor.p.rapidapi.com/locations/auto-complete"

querystring = {"input":"new york"}

headers = {
    'x-rapidapi-key': "5a3c603678msh79fc02407aba28bp1fef39jsn97a1ee136497",
    'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

new_entry = {
    "Address": "1317 Prado St.",
    "Price": 500000,
    "Bedrooms": 3,
    "Baths": 2,
    "Schools": 2,
}
print(my_data.append(new_entry, ignore_index=True))
my_data = my_data.append(new_entry, ignore_index=True)
# response = requests.request("GET", url, headers=headers, params=querystring)
# pprint(response.json())
print(my_data)
# print(response.text)