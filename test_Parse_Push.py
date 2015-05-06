__author__ = 'cesar'


import requests
import pprint
import json

headers = {
           'X-Parse-Application-Id': 'vewdKbKAPt6y9ufviEEYHlq62dXhlEAPldiwNi5P',
           'X-Parse-REST-API-Key': 'XBs6U4aoAgNCZtXnupadG7b74UvglZGCPvOu2x8C',
           'Content-Type': 'application/json'
          }


payload = json.dumps({
    "where": {
         "installationId": "441e7b13-0cf3-4d6f-91ba-4a53cb19d088"
       },
       "data": {
         "alert": "Your suitcase has been filled with tiny apples!"
       }
     })



r = requests.post("https://api.parse.com:443/1/push", data=payload, headers=headers)


pp = pprint.PrettyPrinter(4)
pp.pprint(r.json())