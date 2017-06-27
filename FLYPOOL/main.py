#!/usr/bin/python3.5
# coding: utf-8

import requests, json, sys, os
from time import gmtime, strftime
from lxml import etree

#os.system("clear")

tree = etree.parse("data.xml")
#for user in tree.xpath("/users/user/wallet"):
#    print(user.text)

def getinfo(arg) :
        alloa = etree.parse("data.xml")
        for user in alloa.xpath('/users/user/{}'.format(arg)):
                lll = (user.text)
        return lll

def mnu():
        print("----------------------------------------------------------------")
        print('| Wallet : {}\tPool : {} |'.format(getinfo("wallet"), getinfo("pool")))
        print("----------------------------------------------------------------")
        print('| Exchange : {}\tCurrency : {}\t\t\t\t|'.format(getinfo("exchange"), getinfo("currency")))
        print("----------------------------------------------------------------")


mnu()
