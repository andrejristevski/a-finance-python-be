#!/usr/bin/python

import requests , json ,datetime ,time , ast
import dbService
import mongoRepo
import config

from datetime import date, timedelta
from pymongo import MongoClient


class CurrencyDownloader:

        

    def downloadMissingDataForCurrency(self, currencyConfig):    

        repo = mongoRepo.Repo(currencyConfig)
        service = dbService.DbService(repo)
        latestDownloadedDateInfo = service.getLatestDownloadedDate()
        errors = []
        if latestDownloadedDateInfo is  None:
            date = datetime.datetime(2000, 1, 1)
            service.saveMetaDataObject({'latestDownloadedDate': date})
            latestDownloadedDateInfo = service.getLatestDownloadedDate()   

        latestDownloadedDate = latestDownloadedDateInfo['latestDownloadedDate']

        def isTodayLatestDownloaded(latest):
             now = datetime.datetime.now()
             if latest.year == now.year and latest.month == now.month and latest.day == now.day:
                 return True
             else:
                 return False 

        if isTodayLatestDownloaded(latestDownloadedDate):
            print "Already all downloaded"
            return
        

        def getStringDates( d1, d2):
            dates = []
            delta = d2 - d1
            for i in range(delta.days + 1):
                stringDate= d1 + timedelta(days=i)
                strdate = stringDate.strftime("%Y-%m-%d")
                dates.append(strdate)
            if len(dates) > 0 :
                del dates[0]   
            return dates   


        def downloadDateData(day):
            
            baseUrl = config.getConfigParameter('restApiRatesUrl')
            if currencyConfig['currency'] == 'EUR':
                url = baseUrl+'/'+day
            else:
                url = baseUrl+'/'+day+'?base='+ currencyConfig['currency']

            obj = 'a'
            try:
                a = requests.get(url)
                obj = a.json()
            except:
                errors.append(url)
            return obj


        def saveValues(dataList):
            service.saveMultipleRates(dataList)

        def updateMetaData(id ,date):
            service.updateMetaData(id, date)


        def downloadMissingData():
            daysRates = []
            latestDownloadedDate = latestDownloadedDateInfo['latestDownloadedDate']
            now = datetime.datetime.now()
            stringDatesRange = getStringDates(latestDownloadedDate,now)
            for day in stringDatesRange:
                dayData = downloadDateData(day)
                dayData['exactDate']=datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:]))
                dayData['exactDateStr']=day
                daysRates.append(dayData)
                print day
                time.sleep(.3)
            saveValues(daysRates)
            print 'updateting metadata'
            updateMetaData(latestDownloadedDateInfo['_id'] , daysRates[-1]['exactDate'])

        try:
            downloadMissingData()
        except:
            errors.append('Error downloading daata')


        if len(errors) > 0 :
            print 'imase greski'
        else :
            print 'SUCCESS downloading dates'    



# go through all suported currencies and download 
downloader= CurrencyDownloader()

for currencyConfig in config.getConfigParameter('currencies'):
    print 'Downloading for '+ currencyConfig['currency']
    downloader.downloadMissingDataForCurrency(currencyConfig)
