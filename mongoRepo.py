import pymongo
import config
import utils


metadataCollection = config.getConfigParameter('metadataCollection')
dbName = config.getConfigParameter('dbName')
retesCollection = config.getConfigParameter('ratesCollection')

class Repo(object):

    type = 'MongoDb'
  

    def __init__(self , host =config.getConfigParameter('host') , port=config.getConfigParameter('port')):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[dbName]
    
    def getLatestDownloadedDate(self):
        date = self.db[metadataCollection].find_one()
        if date is not None:
            return utils.removeUnicodeFromDict(date)
        else:
            return None


    def getRatesBetweenDates(self , d1 ,d2):
        res = self.db[retesCollection].find({"exactDate":{"$gt" : d1,"$lte" : d2}})
        removedUnicode = utils.removeUnicodeFromList(res)
        return removedUnicode 
        # self.db[retesCollection].find({"exactDate":{$gt : ISODate("2017-07-29T00:00:00Z"),$lt:ISODate("2010-07-23T00:00:00Z")}})

    def saveRatesForDate(self ,date , rates):
        return

    def saveMultipleRates(self ,data):
        self.db[retesCollection].insert(data)    

    def saveMetaDataObject(self,data):    
        self.db[metadataCollection].insert(data)   

    def updateMetaData(self, id, data):
        a=0
        self.db[metadataCollection].update({'_id':id},{'latestDownloadedDate': data})     