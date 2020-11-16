import pandas as pd
import requests
from pprint import pprint

url = "https://realtor.p.rapidapi.com/locations/auto-complete"

querystring = {"input":"new york"}

headers = {
    'x-rapidapi-key': "5a3c603678msh79fc02407aba28bp1fef39jsn97a1ee136497",
    'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

# add property function
def add_address(address, price, schools, bedrooms, baths):
    my_data = pd.read_csv("data.csv")
    new_entry = {
    "Address": address,
    "Price": price,
    "Bedrooms": bedrooms,
    "Baths": baths,
    "Schools": schools,
    }
    my_data = my_data.append(new_entry, ignore_index=True)
    my_data.to_csv('data.csv', index = False, header=True)

# Differerent ways to add a a propery (Only run function if need to add property)
# add_address("1318 Prado St.", 500000 , 2, 3, 2) 
# add_address(address = "1324 Prado St.", bedrooms = 3 ,price = 500000 , baths = 3, schools = 5)

# Temp/Dummy Data
# new_entry = {
#     "Address": "1317 Prado St.",
#     "Price": 500000,
#     "Bedrooms": 3,
#     "Baths": 2,
#     "Schools": 2,
# }

# This call the Api request, Has to be commented out so that we dont pass our set limits for request
# response = requests.request("GET", url, headers=headers, params=querystring)
# pprint(response.json())