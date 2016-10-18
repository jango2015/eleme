from pymongo import MongoClient
client = MongoClient(host='localhost',port=27017)
db = client.get_database('JangoMp')

def Insert(items,collectionName='Spider_zhao_baidu_jobs'):
    collection = db.get_collection(collectionName)
    collection.insert(items)

# def Update(item):
#      collection.update(item)