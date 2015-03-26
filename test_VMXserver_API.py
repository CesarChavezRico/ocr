__author__ = 'cesar'


import requests
import pprint

r = requests.post("http://172.17.0.69:8081", data='{"command":"list_models"}')
# r = requests.post("http://172.17.0.67:8081", data='{"command":"get_params"}')

pp = pprint.PrettyPrinter(4)
pp.pprint(r.json())