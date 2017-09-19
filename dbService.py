
class DbService(object):

    def __init__(self , repo):
        self.repo = repo

    def getLatestDownloadedDate(self):
        return self.repo.getLatestDownloadedDate()

    def getRatesBetweenDates(self , d1, d2, inpCur):
        return self.repo.getRatesBetweenDates(d1,d2)

    def saveRatesForDate(self, date , rates):
        return self.repo.saveRatesForDate(date , rates)

    def saveMultipleRates(self, rates):
        return self.repo.saveMultipleRates(rates)

    def saveMetaDataObject(self,data):    
        self.repo.saveMetaDataObject(data)

    def updateMetaData(self ,id , data):
        self.repo.updateMetaData(id, data)    
    
    