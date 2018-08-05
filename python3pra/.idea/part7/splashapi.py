__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
url = 'http://localhost:8050/render.html?url=https://www.baidu.com&wait=5'
response=requests.get(url)
print(response.text)