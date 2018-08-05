__author__ = 'WQ'
# *_*coding:utf-8 *_*
import pymongo
from bson.objectid import ObjectId
#mongodb连接
client=pymongo.MongoClient(host='localhost',port=27017)
#指定数据库
db=client.test
#指定集合
collection=db.students
'''
#插入数据
student={
    'id':'10001',
    'name':'james',
    'age':20,
    'gender':'male'
}
student1={
    'id':'10002',
    'name':'jamesh',
    'age':21,
    'gender':'male'
}
student2={
    'id':'10003',
    'name':'wade',
    'age':20,
    'gender':'male'
}
student3={
    'id':'10004',
    'name':'curry',
    'age':21,
    'gender':'male'
}
result=collection.insert_many([student2,student3])
print(result.inserted_ids)
print(result)

#查询
result=collection.find_one({'name':'james'})
print(type(result))
print(result)
result=collection.find_one({'_id': ObjectId('5b4ff8bb94c76771c84bec0f')})#法二
print(result)

#查找多个
results=collection.find({'age':20})
print(results)
for result in results:
    print(result)

#查找多个大于20
results=collection.find({'age':{'$gt':20}})
print(results)
for result in results:
    print(result)

#利用正则匹配查询
results=collection.find({'name':{'$regex':'^j.*'}})
print(results)
for result in results:
    print(result)

#属性是否存在
results=collection.find({'name':{'$exists':True}})
print(results)
for result in results:
    print(result)


#计数
count=collection.find().count()
print(count)

count=collection.find({'age':20}).count()
print(count)

#排序

results=collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])

#偏移

results=collection.find().sort('name',pymongo.ASCENDING).skip(2)#偏移2
print([result['name'] for result in results])

results=collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)#偏移2，限制2
print([result['name'] for result in results])


#更新
condition={'id':'10001'}
student=collection.find_one(condition)
student['name']='lebron'
result=collection.update(condition,student)
print(result)
#官方推荐方法
condition={'id':'10001'}
student=collection.find_one(condition)
student['name']='lebrons'
result=collection.update_one(condition,{'$set':student})
print(result)
#更新条件
condition={'age':{'$gt':20}}
result=collection.update_many(condition,{'$inc':{'age':1}})
print(result)
'''

#删除
result=collection.delete_one({'name':'curry'})#删除一个,多个用delete_many
print(result)
print(result.deleted_count)