import dbService
import mongoRepo
import config
import calcUtils
from datetime import date, timedelta

currencies = config.getConfigParameter('currencies')
currencyConfig=currencies[0]
repo = mongoRepo.Repo(currencyConfig)
service = dbService.DbService(repo)

"""
Entry points for calculations

"""

def getCurrencyPairData(startDate, endDate, inpCur, outCur):
    setCorrectCurrency(inpCur)

    rates = service.getRatesBetweenDates(startDate, endDate, inpCur)
    deleteId(rates)

    # mean = calcUtils.CalcUtils.findMeanForCurrency(res, outCur[0])
    datasets = []
    for c in outCur:
        dataset = buildDataSetForCur(inpCur, c, rates)
        datasets.append(dataset)

    labels = getLabels(rates)    

    print("returning dates bettween", startDate, "and", endDate, "for", inpCur)
    return {
        'datasets': datasets,
        'labels': labels}

def getCurrencyStrenght(startDate, endDate, inpCur, outCur):
    rates = service.getRatesBetweenDates(startDate, endDate, inpCur)
    deleteId(rates)



    return rates

"""

END of entry points for calculations

"""

def getLabels(rates):
    res = []
    for item in rates:
        res.append(item['exactDateStr'])
    return res    


def buildDataSetForCur(inpCur, c, rates):
    mean = calcUtils.CalcUtils.findMeanForCurrency(rates, c)
    values = []
    for item in rates:
        values.append(item['rates'][c])
    return {
        'mean': mean,
        'rates': values,
        'inpCur': inpCur,
        'outputCur': c 
    }    


















def getCurrencyConfig(code):
    currency = [i for i in currencies if i['currency'] == code]
    return currency[0]    


def deleteId(l):
    for element in l:
        try:
            element.pop('_id')
        except KeyError:
            pass

def setCorrectCurrency(cur):   
    if currencyConfig['currency'] != cur:
        print('change')
        newCurrencyConfig = getCurrencyConfig(cur)
        repo.setDb(newCurrencyConfig)    
    else:
        print('same')           