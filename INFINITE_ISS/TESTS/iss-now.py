#!/usr/bin/python3.5
# coding: utf-8

#Prérequis pip install requests

import requests, os, json, datetime
from time import gmtime, strftime

#os.system("clear")

def getnowAPI(arg) :
        r = requests.get("http://api.open-notify.org/iss-now.json")
        paramObj = json.loads(r.text)
        return paramObj[arg]

def getnowAPIpos(arg) :
        r = requests.get("http://api.open-notify.org/iss-now.json")
        paramObj = json.loads(r.text)
        paramObjloc = paramObj["iss_position"]
        return paramObjloc[arg]

def timestampToDate(timestamps, datePattern):
        return strftime("%b %d %Y %H:%M", gmtime(float(timestamps)))

tmstmp = getnowAPI("timestamp")
date = timestampToDate(tmstmp, "%b %d %Y %H:%M")

print('\nDate et heure de la station spacial : {}\n'.format(date))
print("La position de la station est :")
print('\tLongitude : {}'.format(getnowAPIpos("longitude")))
print('\tLatitude : {}\n'.format(getnowAPIpos("latitude")))
