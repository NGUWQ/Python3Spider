__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    #'Host': 'ww3.sinaimg.cn'
}
proxy='119.23.64.49:3128'
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy
}
try:
    response=requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.ConnectionError as e:
    print(e.args)