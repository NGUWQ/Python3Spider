__author__ = 'WQ'
# *_*coding:utf-8 *_*
#request高级用法
import requests
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
url='http://httpbin.org/post'
data={'name':'wang','age':'22'}
files={'file':open('github.ico','rb')}
r=requests.post(url,data=data,headers=headers,files=files)
print(r.text)
