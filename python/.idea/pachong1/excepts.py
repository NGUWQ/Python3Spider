#Created by TTT
import urllib.request
import urllib.error as u
import http.cookiejar
url='http://www.baidu.com'
request=urllib.request.Request(url)
try:
    response=urllib.request.urlopen(request,timeout=10)
except u.HTTPError as e:#URLError的子类
    print(e.code)
except u.URLError as e:
    if hasattr(e,'reason'):
        print(e.reason)


