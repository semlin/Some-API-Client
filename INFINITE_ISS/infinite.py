#!/usr/bin/python3.5
# coding: utf-8

#Prérequis pip install requests

import requests, os, json, datetime
from time import gmtime, strftime

NY = {"lat": 40.71, "lon": -74}
Paris = {"lat": 48.83, "lon": 2.333}

os.system("clear")

def getnowAPI(arg) :
        r = requests.get("http://api.open-notify.org/iss-now.json")
        paramObj = json.loads(r.text)
        return paramObj[arg]

def getnowAPIpos(arg) :
        r = requests.get("http://api.open-notify.org/iss-now.json")
        paramObj = json.loads(r.text)
        paramObjloc = paramObj["iss_position"]
        return paramObjloc[arg]

def getpassAPI(city) :
        response = requests.get("http://api.open-notify.org/iss-pass.json", params=city)
        data = response.json()
        datareq = data["request"]
        dataresp = data["response"]
        nbrpasses = datareq["passes"]
        i = 0
        while i < nbrpasses :
                dataraspa = dataresp[i]
                b = dataraspa["risetime"]
                c = dataraspa["duration"]
                d = timestampToDate(b, "%b %d %Y %H:%M")
                j=i+1
                print("\nPassage n°{} prévu le {}".format(j,d))
                print("Durée de la position {} sec\n".format(c))
                i=i+1
        return

def getastrosAPI() :
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        datapeo = data["people"]
        nbrpeo = data["number"]
        print("\nLa station heberge {} astronautes actuellement :\n".format(nbrpeo))
        i = 0
        while i < nbrpeo :
                datam = datapeo[i]
                a = datam["name"]
                b = datam["craft"]
                j=i+1
                print("\tASTRO{}:{} {}\n".format(j,b,a))
                i=i+1
        return


def timestampToDate(timestamps, datePattern):
        return strftime("%b %d %Y %H:%M", gmtime(float(timestamps)))

tmstmp = getnowAPI("timestamp")
date = timestampToDate(tmstmp, "%b %d %Y %H:%M")

print('\nDate et heure de la station spacial : {}\n'.format(date))
print("La position de la station est :")
print('\tLongitude : {}'.format(getnowAPIpos("longitude")))
print('\tLatitude : {}\n'.format(getnowAPIpos("latitude")))
print("Prochain passage proche de Paris :")
getpassAPI(Paris)
getastrosAPI()
