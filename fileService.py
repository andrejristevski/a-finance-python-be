#!/usr/bin/python

# Enrich data.json 

import requests , json ,datetime ,time
import dbService
from datetime import date, timedelta
from pymongo import MongoClient

client = MongoClient()
db=client.pytdb

# rates = db.rates
rate = db.test

now = datetime.datetime.now()
print now
d1 = date(2000, 1, 1)  # start date
d2 = date(now.year, now.month, now.day)  # end date
# d2 = date(2000, 1, 3)  # end date

delta = d2 - d1         # timedelta
dates = []


def getdates():
    for i in range(delta.days + 1):
       dateUrl = d1 + timedelta(days=i)
    #    print(d1 + timedelta(days=i))
       strdate = dateUrl.strftime("%Y-%m-%d")
       dates.append(strdate)

getdates()

with open('data.json', 'r') as file:
    content = file.read()
    listOfValues = json.loads(content)
    for i in range(len(listOfValues)) :
        dayValue=listOfValues[i]
        dayValue['exactDate']=datetime.datetime(int(dates[i][:4]), int(dates[i][5:7]), int(dates[i][8:]))
        dayValue['exactDateStr']=dates[i]
    file.close()

with open('data.json', 'w+') as file:    
    # json.dump(listOfValues, file)    


rate.insert(listOfValues)
