#!/usr/bin/python3.5
# coding: utf-8

#Prérequis pip install requests

import requests, os, json, datetime, sys
from time import gmtime, strftime

chx = ""
mnu = 0

os.system("clear")

def clearScreen():
	os.system("clear")
	return

def retourMenu(arg):
	global mnu
	if arg == 1 :
		mnu = 0
		mnu = int(mnu)
		return menu()

	elif arg == 2 :
		return sys.exit()

	else :
		print("\tErreur de saisie, caractère non pris en charge\t")
		retrnMnu = raw_input("\n\n1 : Menu\t2 : Exit\n")
		retrnMnu = int(retrnMnu)
		return retourMenu(retrnMnu)

def menu() :
	global mnu
	if mnu == 0 :
		clearScreen()
		print("\nWelcome to ISS Infinite\n\t1° Afficher les info ISS actuels\n\t2° Afficher les prochains passages\n\t3° Afficher les astronautes présents\n\t4° Exit\n")
		mnu = raw_input("Entre une valeurs numérique :\n")
		mnu = int(mnu)
		return menu()

	elif mnu == 1 : 
		clearScreen()
		print("La position de la station est :")
		print('\tLongitude : {}'.format(getnowAPIpos("longitude")))
		print('\tLatitude : {}\n'.format(getnowAPIpos("latitude")))
		retrnMnu = raw_input("\n\n1 : Menu\t2 : Exit\n")
		retrnMnu = int(retrnMnu)
		return retourMenu(retrnMnu)

	elif mnu == 2 : 
		clearScreen()
		chx = raw_input("Pour savoir quand la station passera au dessus de votre ville\nVeuillez entrer le nom de votre ville :\n")
		getParams(chx)
		retrnMnu = raw_input("\n\n1 : Menu\t2 : Exit\n")
		retrnMnu = int(retrnMnu)
		return retourMenu(retrnMnu)

	elif mnu == 3 : 
		clearScreen()	
		getastrosAPI()
		retrnMnu = raw_input("\n\n1 : Menu\t2 : Exit\n")
		retrnMnu = int(retrnMnu)
		return retourMenu(retrnMnu)

	elif mnu == 4 :
		return sys.exit()

	else :
		clearScreen()
		print("\tErreur de saisie, caractère non pris en charge(else menu)\t")
		retrnMnu = raw_input("\n\n1 : Menu\t2 : Exit\n")
		retrnMnu = int(retrnMnu)
		return retourMenu(retrnMnu)

def getParams(arg) :
        json_data=open('someCity.json').read()
        data = json.loads(json_data)
        datacity = data[arg]
        return getpassAPI(datacity)

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

clearScreen()
menu()
