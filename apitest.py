#!/usr/bin/env python3

import requests
import json

scheme_code = '101206'

api = f'https://api.mfapi.in/mf/{scheme_code}'

response = requests.get(api)

#file = open('apiresponse.txt', 'w+')
#for line in response.text:
#    file.write(line)
#print(response.text)

dict_response = json.loads(response.text)
dict_response = dict_response["data"]

for onedict in dict_response:
    if onedict['date'] == '22-04-2006':
        start = onedict['nav']
    if onedict['date'] == '02-04-2006':
        end = onedict['nav']

print(start, end)