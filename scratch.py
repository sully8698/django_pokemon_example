# practice for 3rd party api requests

import requests
from requests_oauthlib import OAuth1
import pprint  #shows just the keys and pretties up the consol print from json
from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ['NOUN_KEY'])

pp = pprint.PrettyPrinter(indent=2, depth=2) #only go 2 levels deep in the json data is what this is saying


endpoint = "https://api.thenounproject.com/v2/icon?query=ultraball"
response = requests.get(endpoint, auth=auth)
responseJSON = response.json()
pp.pprint(responseJSON)