#!/usr/bin/python



import requests , json ,datetime ,time
import dbService
from datetime import date, timedelta
from pymongo import MongoClient

client = MongoClient()
db=client.pytdb
collection = db.rates
sc = db.backup

values = list(collection.find())

sc.insert(values) 
