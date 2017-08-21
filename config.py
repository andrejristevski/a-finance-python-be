config = {
    'port' : 27017,
    'host' : 'localhost',
    'metadataCollection' : 'metaData',
    'dbName' : 'pytdb',
    'restApiRatesUrl' : 'http://api.fixer.io/',
    'ratesCollection' : "rates",
    'currencies': 
        [{
            'metadataCollection' : 'metaData',
            'ratesCollection' : "rates",
            'dbName' : 'pytdb',
            'currency': 'EUR'
        },
        {
            'metadataCollection' : 'metaDataUSD',
            'ratesCollection' : "ratesUSD",
            'dbName' : 'pytdb',
            'currency': 'USD',        
         },
         {
            'metadataCollection' : 'metaDataAUD',
            'ratesCollection' : "ratesAUD",
            'dbName' : 'pytdb',
            'currency': 'AUD',        
         },
          {
            'metadataCollection' : 'metaDataCAD',
            'ratesCollection' : "ratesCAD",
            'dbName' : 'pytdb',
            'currency': 'CAD',        
         },
          {
            'metadataCollection' : 'metaDataJPY',
            'ratesCollection' : "ratesJPY",
            'dbName' : 'pytdb',
            'currency': 'JPY',        
         },
          {
            'metadataCollection' : 'metaDataCNY',
            'ratesCollection' : "ratesCNY",
            'dbName' : 'pytdb',
            'currency': 'CNY',        
         },
         ]
}

def getConfigParameter(key):
    if key in config:
        return config[key]
    else:
        print "Nonexisting key"    