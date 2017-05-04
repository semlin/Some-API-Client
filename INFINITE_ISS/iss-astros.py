#!/usr/bin/python3.5
# coding: utf-8

import requests, os, json, datetime
from time import gmtime, strftime

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

getastrosAPI()
