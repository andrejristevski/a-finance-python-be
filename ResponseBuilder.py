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

    mean = calcUtils.CalcUtils.findMeanForCurrency(rates, outCur[0])
    datasets = []
    for c in outCur:
        dataset = buildDataSetForCurPair(inpCur, c, rates)
        datasets.append(dataset)

    labels = getLabels(rates)    

    print("returning dates bettween", startDate, "and", endDate, "for", inpCur)
    return {
        'datasets': datasets,
        'labels': labels
        }



def getCurrencyStrenght(startDate, endDate, inpCur, outCur):
    rates = service.getRatesBetweenDates(startDate, endDate, inpCur)
    deleteId(rates)

    datasets = []
    for c in outCur:
        dataset = buildDataSetForCurStrength(inpCur, c, rates)
        datasets.append(dataset)

    labels = getLabels(rates)
    return {
        'datasets': datasets,
        'labels': labels
        }


def getPercentageSum(startDate, endDate, inpCur, outCur):
    
    datasets = []
    for c in outCur:
        setCorrectCurrency(c)
        rates = service.getRatesBetweenDates(startDate, endDate, c)
        deleteId(rates)
        # edna valuta sproti site 
        dataset = buildDataSetForPercentageSum(c, rates, outCur)
        datasets.append(dataset)


    rates = service.getRatesBetweenDates(startDate, endDate, inpCur)
    labels = getLabels(rates)
    return {
        'datasets': datasets,
        'labels': labels
        }



"""

END of entry points for calculations

"""


def buildDataSetForPercentageSum(c, rates, outCur):
    res = []
    curenciesPercentigase = []
    for testAgainst in outCur:
        
        if c is not testAgainst:
            curBaseRate = rates[0]['rates'][testAgainst]
            curRates = getSingleValuedRatesForCur(rates, testAgainst)

            # procenti za evro sprema dolar
            currencyPerValues = []
            for rate in curRates:
                percentageChanged = abs(curBaseRate-rate)/curBaseRate*100
                sign = -1 if rate < curBaseRate else 1
                currencyPerValues.append(sign*percentageChanged)
            curenciesPercentigase.append(currencyPerValues)    
    
    for i in range(len(curenciesPercentigase[0])):
        percentageSum = 0;
        for x in range(len(curenciesPercentigase)):
            percentageSum += curenciesPercentigase[x][i]

        res.append(percentageSum)

    return {
        'rates': res,
        'inpCur': c,
        'outputCur': 'all' 
    }         


def buildDataSetForCurPair(inpCur, c, rates):
    values = getSingleValuedRatesForCur(rates, c)
    return {
        'rates': values,
        'inpCur': inpCur,
        'outputCur': c 
    }    

def buildDataSetForCurStrength(inpCur, c, rates):
    if c is not inpCur:
        curBaseRate = rates[0]['rates'][c]
        curRates = getSingleValuedRatesForCur(rates, c)
        res = []
        for rate in curRates:
            percentageChanged = abs(curBaseRate-rate)/curBaseRate*100
            sign = -1 if rate < curBaseRate else 1
            res.append(sign*percentageChanged)
    return {
        'rates': res,
        'inpCur': inpCur,
        'outputCur': c 
    }      
    

def getSingleValuedRatesForCur(rates, c):
    values = []
    for item in rates:
        try:
            values.append(item['rates'][c])
        except:
            pass    
    return values    


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
    print('setting cur to '+cur) 
    global currencyConfig 
    if currencyConfig['currency'] != cur:
        newCurrencyConfig = getCurrencyConfig(cur)
        repo.setDb(newCurrencyConfig)
        currencyConfig = newCurrencyConfig
    else:
        print('same')  


def getLabels(rates):
    res = []
    for item in rates:
        res.append(item['exactDateStr'])
    return res          