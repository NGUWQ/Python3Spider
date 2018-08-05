__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
import re
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
url='https://github.com/favicon.ico'
r=requests.get(url,headers=headers)
with open('github.ico','wb') as f:
    f.write(r.content)
f.close()

