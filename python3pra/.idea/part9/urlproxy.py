__author__ = 'WQ'
# *_*coding:utf-8 *_*
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    #'Host': 'ww3.sinaimg.cn'
}
proxy='119.23.64.49:3128'
proxy_handler=ProxyHandler({
    'http':'http://'+proxy,
    'https':'https://'+proxy
})
opener=build_opener(proxy_handler)
try:
    response=opener.open('http:www.zhihu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)