__author__ = 'WQ'
# *_*coding:utf-8 *_*
import pymysql
db=pymysql.connect(host='localhost',user='root',password='123',port=3306,db='spiders')
cursor=db.cursor()
'''
#创建表
sql='CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL ,name VARCHAR(255) NOT NULL ,age INT NOT NULL ,PRIMARY KEY(id))'
cursor.execute(sql)
db.close()
'''
'''
#插入数据
id='10001'
user='Mike'
age=20
sql='INSERT INTO students(id,name,age) VALUES (%s,%s,%s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
#db.close()

#插入数据2
data={
    'id':'10002',
    'name':'james',
    'age':33,
}
table='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
#db.close()
'''
'''
#更新数据,不存在就添加
data={
    'id':'10002',
    'name':'james',
    'age':34,
}
table='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='INSERT INTO {table}({keys}) VALUES ({values}) ON  DUPLICATE KEY  UPDATE '.format(table=table,keys=keys,values=values)
update=','.join([" {key} =%s".format(key=key) for key in data])
sql+=update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
#db.close()

#删除数据
table='students'
condition='age>20'
sql='DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
'''
#查询数据
sql='SELECT * FROM students WHERE  age>=20'
try:
    cursor.execute(sql)
    print('count:',cursor.rowcount)#获取查询结果的条数
    print(cursor.fetchone())#获取结果的第一条数据
    print(cursor.fetchall())#获取结果的所有数据
except:
    print('error')