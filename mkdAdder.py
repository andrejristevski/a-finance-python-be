#!/usr/bin/python
import pymongo
import config
import utils

client = pymongo.MongoClient()

def addMKDToCollection(dbConfig):
    db = client[dbConfig['dbName']]
    currency = dbConfig['currency']

    for element in db[dbConfig['ratesCollection']].find({}):
        mkdVal = element['rates']['EUR'] * 61.5
        db[dbConfig['ratesCollection']].update({"_id": element["_id"]},{ "$set": { "rates.MKD": mkdVal }})



for currencyConfig in config.getConfigParameter('currencies'):
    print('Updating for '+ currencyConfig['currency'])
    if currencyConfig['currency'] is not 'EUR':
        addMKDToCollection(currencyConfig)