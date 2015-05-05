__author__ = 'Cesar'

import pprint

from apiclient.discovery import build



api_root = 'https://ocr-backend.appspot.com/_ah/api'
api = 'backend'
version = 'v1'
discovery_url = '%s/discovery/v1/apis/%s/%s/rest' % (api_root, api, version)
print discovery_url
backend = build(api, version, discoveryServiceUrl=discovery_url)

payload = {"account_number": "33"}

request = backend.meter().create(body=payload)
response = request.execute()
pprint.pprint(response)
