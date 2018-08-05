__author__ = 'WQ'
# *_*coding:utf-8 *_*
import csv
import pandas

#csv写入读取数据
with open('test.csv', 'w',newline='') as csvfile:
    
    filename=['id', 'name', 'age']
    writer = csv.DictWriter(csvfile,fieldnames=filename)
    writer.writeheader()
    writer.writerow({'id':'10001','name':'jordan','age':'22'})
with open('test.csv', 'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)
'''
#pandas写入读取数据
da=['id', 'name', 'age']
content=[['10001','jordan','22'],['10002','jorda','21'],['10003','jord','20']]
df=pandas.DataFrame(content,columns=da)
df.to_csv('test.csv',encoding='utf-8')
df=pandas.read_csv('test.csv',encoding='utf-8')
print(df)
'''