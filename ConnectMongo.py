#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb  #连接mydb数据库，没有则自动创建
my_set=db.test_set #使用test_set集合，没有则自动创建
#插入
my_set.insert({"name":456})
users=[{"name":123,"age":18},{"name":789,"age":19}]
my_set.insert(users)

#查询
for i in my_set.find():
    print(i)
for i in my_set.find({"name":123}):
    print(i)
for i in my_set.find({"name":123},{"name":1,"_id":0}):
    print(i)
print(my_set.find_one({"name":789}))

#更新
my_set.update({"name": 123},{"$set":{"age": 21}},upsert=False,multi=True)


#删除
# my_set.remove()
my_set.remove({"name":456})
id=my_set.find_one({"name":789})["age"]
my_set.remove(id)

for i in my_set.find({"age":{"$gt":20}}):
    print (i)

for i in my_set.find().sort([("age",-1)]):
    print (i)

for i in my_set.find({"age":{"$in":(19,20)}}):
    print (i)

for i in my_set.find({"$or":[{"age":21},{"age":18}]}):
    print(i)