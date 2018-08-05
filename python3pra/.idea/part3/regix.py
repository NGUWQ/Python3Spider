__author__ = 'WQ'
# *_*coding:utf-8 *_*
import re
content='''hello 1234567
 haha
'''
result=re.match('^he.*?(\d+).*?haha$',content,re.S)
print(result.group(1))
