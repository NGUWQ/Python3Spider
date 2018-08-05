#Created by TTT
import urllib.request
import http.cookiejar as c
'''
3.从文件中获取Cookie并访问
filename='mycookie.txt'
url='http://www.baidu.com'
cookie=c.MozillaCookieJar()
cookie.load(filename,ignore_expires=True,ignore_discard=True)
request=urllib.request.Request(url)
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response=opener.open(request)
print(response.read())
'''
'''
2.保存cookie到文件
filename='mycookie.txt'
cookie=c.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
openner=urllib.request.build_opener(handler)
url='http://www.baidu.com'
request=urllib.request.Request(url)
response=openner.open(request)
cookie.save(ignore_discard=True,ignore_expires=True)
'''
'''
1.获取cookie保存到变量
#声明一个CookieJar对象实例来保存cookie
cookie=c.CookieJar()
#利用urllib.request库中的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener=urllib.request.build_opener(handler)
url='http://www.baidu.com'
request=urllib.request.Request(url)
response=opener.open(request)
for item in cookie:
    print('Name='+item.name)
    print('Value'+item.value)
'''