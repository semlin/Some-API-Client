#!/usr/bin/python3.5
# coding: utf-8

#Prérequis pip install requests

import requests, os, json, datetime
from time import gmtime, strftime

NY = {"lat": 40.71, "lon": -74}
Paris = {"lat": 48.83, "lon": 2.333}

####### COMON #######
def timestampToDate(timestamps, datePattern):
        return strftime("%b %d %Y %H:%M", gmtime(float(timestamps)))
#####################


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

#print('\tReponse : {}\n'.format(getpassAPI(Paris)))
getpassAPI(Paris)
