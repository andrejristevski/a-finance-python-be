#!/usr/bin/python

# backtester
# prima niza od data i strategija 
# vrvi niz nizata i ja exekutira strategijata

import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import pandas as pd
import ResponseBuilder, datetime

d1 = datetime.datetime(2015, 6, 26)
d2 = datetime.datetime(2017, 7, 26)
d3 = datetime.datetime(2013, 7, 26)

# ResponseBuilder.getPercentageSum(d1, d2, 'EUR', ['AUD', 'EUR', 'USD'])

# simpleRates = ResponseBuilder.getCurrencyPairData(d1, d2 , 'EUR', ['AUD', 'USD']) 
currencyLaderRates = ResponseBuilder.getPercentageSum(d3, d2, 'EUR', ['AUD', 'EUR', 'USD'])

# showcase 
# df = pd.DataFrame(simpleRates['datasets'][0])
# print(df.head())
# df['avg10'] = df['rates'].rolling(window=10, min_periods=1 , center=False).mean()
# df['avg20'] = df['rates'].rolling(window=20, min_periods=1 , center=False).mean()
# print(df)

# x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in simpleRates['labels']]
# plt.plot(x, simpleRates['datasets'][0]['rates'], color='g')
# plt.plot(x, df['avg10'], color='b')
# plt.plot(x, df['avg20'], color='r')
# print(df)
# plt.show()


df = pd.DataFrame(currencyLaderRates['datasets'][0])
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in currencyLaderRates['labels']]
plt.plot(x, currencyLaderRates['datasets'][0]['rates'], color='g')

for line in currencyLaderRates['datasets']:
    plt.plot(x, line['rates'])

plt.show()

# THIS IS INTERFACE for strategy pattern
class Strategy:
    def __init__(self, func=None):
        if func:
             self.execute = func

    def execute(self):
        self.execute()

class DataInterface:
    def __init__(self, data, nextDataPoint):
        self.data = data
        self.nextDataPoint = nextDataPoint


class Account:
    def __init__(self):
        self.a = a
        

# Test
def printa(datasets, a):
    print(len(datasets))
    return sum(datasets)

def printb(datasets):
    print(len(datasets))
    return sum(datasets)

d1 = [1,2,3,4]
d2 = [3,4]

strat1 = Strategy( printa )
strat2 = Strategy( printb )

xa = strat1.execute(d1, 15)
ya = strat2.execute(d2)
print(xa,ya)
# end of showcase





