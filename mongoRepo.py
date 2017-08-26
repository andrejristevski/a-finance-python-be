import pymongo
import config
import utils



class Repo(object):

    type = 'MongoDb'
  


    def __init__(self, dbConfig, host =config.getConfigParameter('host') , port=config.getConfigParameter('port') ):
        self.client = pymongo.MongoClient(host, port)
        self.setDb(dbConfig)
        
    def setDb(self, dbConfig):
        self.db = self.client[dbConfig['dbName']]
        self.dbConfig = dbConfig

    def getLatestDownloadedDate(self):
        date = self.db[self.dbConfig['metadataCollection']].find_one()
        if date is not None:
            return utils.removeUnicodeFromDict(date)
        else:
            return None


    def getRatesBetweenDates(self , d1 ,d2):
        res = self.db[self.dbConfig['ratesCollection']].find({"exactDate":{"$gt" : d1,"$lte" : d2}})
        removedUnicode = utils.removeUnicodeFromList(res)
        return removedUnicode 
        # self.db[retesCollection].find({"exactDate":{$gt : ISODate("2017-07-29T00:00:00Z"),$lt:ISODate("2010-07-23T00:00:00Z")}})

    def saveRatesForDate(self ,date , rates):
        return

    def saveMultipleRates(self ,data):
        self.db[self.dbConfig['ratesCollection']].insert(data)    

    def saveMetaDataObject(self,data):    
        self.db[self.dbConfig['metadataCollection']].insert(data)   

    def updateMetaData(self, id, data):
        self.db[self.dbConfig['metadataCollection']].update({'_id':id},{'latestDownloadedDate': data})     