__author__ = 'WQ'
# *_*coding:utf-8 *_*
from redis import  StrictRedis
redis=StrictRedis(host='localhost',port=6379,db=0,password=None)
redis.set('name','Bob')
print(redis.get('name'))