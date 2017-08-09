#!/usr/bin/python
from flask import Flask , jsonify , request

import requests , json ,datetime ,time
import dbService
import mongoRepo
from datetime import date, timedelta
from flask_cors import CORS, cross_origin


repo = mongoRepo.Repo()
service = dbService.DbService(repo)

app = Flask(__name__)
CORS(app)

def preparePayLoad(l):
    for el in l:
        try:
            el.pop('_id')
        except KeyError:
            pass


@app.route('/a')
def index () :

    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')

    print startDate
    print endDate
    print 'shit sun'

    d1= datetime.datetime(int(startDate[:4]), int(startDate[5:7]), int(startDate[8:]))
    d2= datetime.datetime(int(endDate[:4]), int(endDate[5:7]), int(endDate[8:]))
    res = service.getRatesBetweenDates(d1,d2)
    preparePayLoad(res)
    print 'returnig sth'
    return jsonify(res)

if __name__ == "__main__" :
    app.run(debug = True)  

