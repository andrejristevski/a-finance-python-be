config = {
    'port' : 27017,
    'host' : 'localhost',
    'metadataCollection' : 'metaData',
    'dbName' : 'pytdb',
    'restApiRatesUrl' : 'http://api.fixer.io/',
    'ratesCollection' : "rates"
}

def getConfigParameter(key):
    if key in config:
        return config[key]
    else:
        print "Nonexisting key"    