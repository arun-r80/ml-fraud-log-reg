# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:36:03 2018

@author: tperiyas
"""

import json, requests, pprint

url = 'http://localhost:5000/empdb/employee/101'




data = requests.get(url=url, params='')
binary = data.content
output = json.loads(binary)

# test to see if the request was valid
#print output['status']

# output all of the results
pprint.pprint(output)

# step-by-step directions

for route in output['emp']:
        
                print (route['id'])
                print (route['name'])
                print (route['title'])
