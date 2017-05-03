
#!/usr/bin/python3.5
# coding: utf-8

#Prérequis pip install requests

import requests, os, json

#import sys, os, time
#from datetime import datetime

os.system("clear")

def getnowAPI(arg) :
        # Make a get request to get the latest position of the international space station from the opennotify api.
        r = requests.get("http://api.open-notify.org/iss-now.json")
        # Print the status code of the response.
        print(r.status_code)
        print(r.text)
        paramObj = json.loads(r.text)
        print paramObj["arg"]

echo "test"


#obj = json.loads(r.text)
#print obj['timestamp']

print('getnowAPI(timestamp)')
