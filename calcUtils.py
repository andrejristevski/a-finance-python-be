import numpy as np

class CalcUtils(object):

    @staticmethod
    def findMeanForCurrency(ratesList, cur):
        mean =float( sum(item['rates'][cur] for item in ratesList) /len(ratesList))
        return mean