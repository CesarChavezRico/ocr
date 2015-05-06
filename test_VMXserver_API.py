__author__ = 'cesar'


import requests
import pprint
from detection import Detection

BUCKET = 'ocr-test-pics-cropped'
IMAGE = 'red-a6309a03-aa26-493c-99db-ba68cfa225c8.jpg'


# r = requests.post("http://172.17.0.67:8081", data='{"command":"get_params"}')

r = requests.post("http://172.17.0.64:8081", data='{"command":"get_config"}')

# r = requests.post("http://172.17.0.12:8081", data='{'
#                                                     '"command":"load_model",'
#                                                     '"uuids":'
#                                                         '["560e632c54953b2729ed7c4c951529861b99"],'
#                                                     '"compiled":true'
#                                                  '}')

# data = '{{"command":"process_image", "images":[{{"image":"http://storage.googleapis.com/{0}/{1}"}}]}}'.format(BUCKET,
#                                                                                                               IMAGE)
# r = requests.post("http://172.17.0.12:8081", data=data)

pp = pprint.PrettyPrinter(4)
pp.pprint(r.json())

#
# number = []
#
# for o in r.json()['objects']:
#     if Detection.is_detection(o):
#         number.append(Detection(o))
#
# reading = ''
# for num in sorted(number, key=lambda n: n.center):
#     reading += str(num.value)
#
#
# print reading