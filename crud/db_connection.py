import pymongo
url='mongodb://localhost:27017/djangocrud'
client=pymongo.MongoClient(url)
db=client['test_mongo']