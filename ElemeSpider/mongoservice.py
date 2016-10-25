from pymongo import MongoClient
client = MongoClient(host='localhost',port=27017)
db = client.get_database('Meishijie')

def Insert(items,collectionName='Spider_zhao_baidu_jobs'):
    collection = db.get_collection(collectionName)
    collection.insert(items)

def get_by_pinyin(name,collectionName='Spider_Eleme_Cities_WithGeoHash'):
    collection = db.get_collection(collectionName)
    return collection.find_one({"pinyin":"shanghai"})
def get_all(collectionName='Spider_Eleme_Cities_WithGeoHash'):
    return db.get_collection(collectionName).find()
def get_category_by_cid(cid):
    collection = db.get_collection("Meishijie_shiliao_Categories")
    return collection.find_one({"cid":cid})
# def Update(item):
#      collection.update(item)