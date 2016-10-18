from pymongo import MongoClient
client = MongoClient(host='localhost',port=27017)
db = client.get_database('JangoMp')

def Insert(items,collectionName='Spider_zhao_baidu_jobs'):
    collection = db.get_collection(collectionName)
    collection.insert(items)

def get_by_pinyin(name,collectionName='Spider_Eleme_Cities_WithGeoHash'):
    collection = db.get_collection(collectionName)
    return collection.find_one({"pinyin":"shanghai"})
def get_all(collectionName='Spider_Eleme_Cities_WithGeoHash'):
    return db.get_collection(collectionName).find()
# def Update(item):
#      collection.update(item)