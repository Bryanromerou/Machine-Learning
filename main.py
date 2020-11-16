import pandas as pd
import requests
from pprint import pprint

url = "https://realtor.p.rapidapi.com/locations/auto-complete"

querystring = {"input":"new york"}

headers = {
    'x-rapidapi-key': "5a3c603678msh79fc02407aba28bp1fef39jsn97a1ee136497",
    'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

# response = requests.request("GET", url, headers=headers, params=querystring)
pprint(response.json())
# print(response.text)