#!/usr/bin/python
import pymongo
import config
import utils

client = pymongo.MongoClient()

EURO_VALUE=61.5

def addMKDToCollection(dbConfig):
    db = client[dbConfig['dbName']]
    currency = dbConfig['currency']

    for element in db[dbConfig['ratesCollection']].find({}):
        mkdVal = element['rates']['EUR'] * EURO_VALUE
        db[dbConfig['ratesCollection']].update({"_id": element["_id"]},{ "$set": { "rates.MKD": mkdVal }})

def addMKDToEur(dbConfig):
    db = client[dbConfig['dbName']]
    currency = dbConfig['currency']

    for element in db[dbConfig['ratesCollection']].find({}):
        db[dbConfig['ratesCollection']].update({"_id": element["_id"]},{ "$set": { "rates.MKD": EURO_VALUE }})


for currencyConfig in config.getConfigParameter('currencies'):
    print('Updating for '+ currencyConfig['currency'])
    if currencyConfig['currency'] is not 'EUR':
        addMKDToCollection(currencyConfig)
    else:
        addMKDToEur(currencyConfig)    