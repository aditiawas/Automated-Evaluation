import pymongo

def startInteract():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["python2k18"]
    coll = db["keywords"]
    return client,db,coll

def sendToDb(json):
    client,db,coll=startInteract()
    coll.insert_one(json)

def emptyDb():
    client,db,coll=startInteract()
    coll.delete_many({})

def recvFromDb(num):
    client,db,coll=startInteract()
    scheme=[]
    scheme.append(coll.find_one({"_id":num},{"_id": 0,"question":0,"marks":0}))
    return scheme[0]

def recvAllFromDb():
    client,db,coll=startInteract()
    scheme=[]
    for i in coll.find({},{'_id':1,'question':1,'marks':1}):
        scheme.append(i)
    return(scheme) #change to print to check

def printAll():
    client,db,coll=startInteract()
    scheme=[]
    for i in coll.find():
        scheme.append(i)
    print(scheme) #to check

def findLastId():
    client,db,coll=startInteract()
    getall=coll.find().sort("_id", pymongo.DESCENDING)
    for x in getall:
        return x["_id"]
    else:
        return 0
    
if __name__=="__main__":
    #emptyDb()
    #sendToDb([{"_id":1,"ques":"Random1"}])
    #sendToDb([{"_id":2,"ques":"Random2"}])
    #print(findLastId())
    printAll()
