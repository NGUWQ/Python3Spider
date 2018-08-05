#Created by TTT
#将一个列表写入一个二进制文件中
from pickle import *#pickle(泡菜)
l1=[123,3.3,'nihao',[1,'da']]
'''
filename=open('hehe.pkl','wb')
dump(l1,filename)
'''
filename=open('hehe.pkl','rb')
print(load(filename))

filename.close()