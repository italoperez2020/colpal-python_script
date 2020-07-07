import requests
import json
import sys
from requests.auth import HTTPBasicAuth
import json

url = 'https://api.area1security.com/detections-search'
query="malicious"
days_back="3"
limit="2"

payload ={'query': query, 'days_back':days_back, 'limit': limit}


resp = requests.get(url, params= payload , auth=HTTPBasicAuth('####', '########' ))

response = resp.json()

data = json.dumps(response, indent=4)
print(data)
print(resp.raise_for_status)
