from pymongo import MongoClient
from bson.son import SON
ip='127.0.0.1'
port=27017


client = MongoClient(ip, port)
db = client.zhihu
pipeline = [
            {'$sort': SON([('num', -1)])},
            {'$limit': int(5)}
        ]
x = db['employments'].aggregate(pipeline)
print(type(x))
# top_type = dict(db[type].aggregate(pipeline))
# print(top_type)
# print(list(db[type].aggregate(pipeline)))
# print(db['employments'].find_one())


client.close()