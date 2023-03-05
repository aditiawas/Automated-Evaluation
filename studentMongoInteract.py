import pymongo

def startInteract():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["python2k18"]
    coll = db["students"]
    return client,db,coll

#adds student
def sendToDb(USN):
    client,db,coll=startInteract()
    if not indb(USN):
        json={"_id":findLastId()+1,"USN":USN}
        x = coll.insert_one(json)
        return True
    else:
        return False

def indb(usn):
    x=recvAllFromDb()
    for i in x:
        if i["USN"]==usn:
            return True
    return False

def emptyDb():
    client,db,coll=startInteract()
    coll.delete_many({})

def recvFromDb(num):
    client,db,coll=startInteract()
    detail=[]
    detail.append(coll.find_one({"_id":num},{"_id": 0,"grade": 0}))
    return detail[0]

def recvAllFromDb():
    client,db,coll=startInteract()
    detail=[]
    for i in coll.find():
        detail.append(i)
    return(detail) #to check

def findLastId():
    client,db,coll=startInteract()
    getall=coll.find().sort("_id", pymongo.DESCENDING)
    for x in getall:
        return x["_id"]
    else:
        return 0

def addGrade(num,grade):
    client,db,coll=startInteract()
    coll.update_one({'_id': num}, {'$set': {'grade': grade}})
    
if __name__=="__main__":
    #emptyDb()
    #print(sendToDb("1BM16CS047"))
    #print(recvFromDb(1))
    #addGrade(1,'S')
    #print(recvAllFromDb())
    pass
