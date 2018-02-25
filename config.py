import enviroment

config = {
    'port' : 27017,
    'host' : 'localhost',
    'metadataCollection' : 'metaData',
    'dbName' : 'rates',
    'restApiRatesUrl' : 'https://api.fixer.io/',
    'ratesCollection' : "rates",
    'connectionString': enviroment.getConnectionString(),
    'currencies': 
        [{
            'metadataCollection' : 'metaData',
            'ratesCollection' : "rates",
            'dbName' : 'rates',
            'currency': 'EUR'
        },
        {
            'metadataCollection' : 'metaDataUSD',
            'ratesCollection' : "ratesUSD",
            'dbName' : 'rates',
            'currency': 'USD',        
         },
         {
            'metadataCollection' : 'metaDataAUD',
            'ratesCollection' : "ratesAUD",
            'dbName' : 'rates',
            'currency': 'AUD',        
         },
          {
            'metadataCollection' : 'metaDataCAD',
            'ratesCollection' : "ratesCAD",
            'dbName' : 'rates',
            'currency': 'CAD',        
         },
          {
            'metadataCollection' : 'metaDataJPY',
            'ratesCollection' : "ratesJPY",
            'dbName' : 'rates',
            'currency': 'JPY',        
         },
          {
            'metadataCollection' : 'metaDataCNY',
            'ratesCollection' : "ratesCNY",
            'dbName' : 'rates',
            'currency': 'CNY',        
         },
         ]
}

def getConfigParameter(key):
    if key in config:
        return config[key]
    else:
        print("Nonexisting key")    