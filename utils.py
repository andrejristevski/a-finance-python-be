def removeUnicodeFromDict(obj):
    res = {}   
    for key,value  in obj.items():
        newKey= key.encode('ascii')
        res[newKey] = value
    
    return res    

def removeUnicodeFromList(li):
    res = []
    for el in li:
        res.append(removeUnicodeFromDict(el))    
    return res    
   
