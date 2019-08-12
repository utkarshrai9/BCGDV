import sys
import json
import requests
from datetime import datetime


base_uri = "https://interns.bcgdvsydney.com/"
version = "api/v1/"

r = requests.get(base_uri + version + "key")

data = {
    'name': "Utkarsh Rai",
    'email': "utkarshrai0009@gmail.com",
}

if r.status_code == 200 or r.status_code == 201:
    try:
        response = r.json()
    except Exception as e:
        print("Exception caught, %s", e)
        sys.exit(0)
else:
    print("Oh boy, response is %s and status code is %s", r.text, r.status_code)
    sys.exit(0)
try:
    api_key = response['key']
except KeyError:
    print("Api key not found error, exiting")
    sys.exit(0)
	
try:
    expires = response['expires']
except KeyError:
    print("Expiration not found, continuting")

expires_datetime = datetime.strptime(expires, "%Y-%m-%d %H:%M:%S.%f")

now = datetime.now()

if expires_datetime < now:
    print("Api key already expired")
    # Tried to check the expiration of the key and it was 
	# already expired, so continue without this check.

post_url = base_uri + version + f"submit?apiKey={api_key}"

r = requests.post(post_url, json.dumps(data))

if r.status_code == 202:
    print("Bro, done")
else:
    print(f"Nope, response is {r.text} and status code is {r.status_code}")
