__author__ = 'WQ'
# *_*coding:utf-8 *_*
#连接mysql
import pymysql
db=pymysql.connect(host='localhost',user='root',password='123',port=3306)
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data=cursor.fetchone()
print('database version:',data)
cursor.execute("CREATE DATABASE spiders DEFAULT  CHARACTER  SET  utf8")
db.close()