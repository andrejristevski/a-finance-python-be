#!/usr/bin/python
from flask import Flask , jsonify , request
import requests , json ,datetime ,time
from flask_cors import CORS, cross_origin
import ResponseBuilder

app = Flask(__name__)
CORS(app)


@app.route('/test')
def alive () :
    return "Server is up"

@app.route('/rates', methods=['POST'])
def index () :

    startDate = request.json['startDate']
    endDate = request.json['endDate']
    inpCur = request.json['inp']
    outCur = request.json['out']

    d1 = datetime.datetime(int(startDate[:4]), int(startDate[5:7]), int(startDate[8:]))
    d2 = datetime.datetime(int(endDate[:4]), int(endDate[5:7]), int(endDate[8:]))

    response = ResponseBuilder.getCurrencyPairData(d1, d2, inpCur, outCur)

    return jsonify(response)


# no used
@app.route('/strength', methods=['POST'])
def strength () :

    print('currency strength called')
    inpCur = request.json['inpCur']
    outCur = request.json['outCur']
    startDate = request.json['startDate']
    endDate = request.json['endDate']

    d1 = datetime.datetime(int(startDate[:4]), int(startDate[5:7]), int(startDate[8:]))
    d2 = datetime.datetime(int(endDate[:4]), int(endDate[5:7]), int(endDate[8:]))

    response = ResponseBuilder.getCurrencyStrenght(d1, d2, inpCur, outCur)
    return jsonify(response)


if __name__ == "__main__" :
    app.run(debug = True)  

