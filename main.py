#!/usr/bin/python
from flask import Flask , jsonify , request

import requests , json ,datetime ,time
import dbService
import mongoRepo
from datetime import date, timedelta
from flask_cors import CORS, cross_origin
import config

# EUR
currencies = config.getConfigParameter('currencies')

currencyConfig=currencies[0]

repo = mongoRepo.Repo(currencyConfig)

service = dbService.DbService(repo)

app = Flask(__name__)
CORS(app)


def getCurrencyConfig(code):
    currency = [i for i in currencies if i['currency'] == code]
    return currency[0]


def preparePayLoad(l):
    for element in l:
        try:
            element.pop('_id')
        except KeyError:
            pass


@app.route('/test')
def alive () :
    return "Server is up"

@app.route('/rates', methods=['POST'])
def index () :

    startDate = request.json['startDate']
    endDate = request.json['endDate']
    inpCur = request.json['inp']
    outCur = request.json['out']

    d1= datetime.datetime(int(startDate[:4]), int(startDate[5:7]), int(startDate[8:]))
    d2= datetime.datetime(int(endDate[:4]), int(endDate[5:7]), int(endDate[8:]))

    # this should go to functions so it is used in other charts
    if currencyConfig['currency'] != inpCur:
        print('change')
        newCurrencyConfig = getCurrencyConfig(inpCur)
        # print('New currency config', newCurrencyConfig)
        repo.setDb(newCurrencyConfig)    
    else:
        print('same')    

    res = service.getRatesBetweenDates(d1, d2, inpCur)
    preparePayLoad(res)
    print("returning dates bettween", startDate, "and", endDate, "for", inpCur)
    bdy = {
        'res': res,
        'med': 3 
    }
    return jsonify(bdy)


# no used
@app.route('/strength', methods=['POST'])
def strength () :
    baseCur = request.json['base']
    print(baseCur)
    return 'Success'


if __name__ == "__main__" :
    app.run(debug = True)  

