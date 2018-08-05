#Created by TTT
#利用cookie模拟登陆新浪(失败)
import urllib.request
import urllib.parse
import http.cookiejar as c
filaname='mycookie.txt'
cookie=c.MozillaCookieJar(filaname)
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
data=urllib.parse.urlencode({'loginname':'18872738629',
                             'password':'wq1996122418'}).encode('utf-8')
sinaurl='https://weibo.com/#_loginLayer_1530966056592'
result=opener.open(sinaurl,data)
cookie.save(ignore_discard=True,ignore_expires=True)
sinaurls='http://my.sina.cn/?vt=4&pos=108&his=0'
result=opener.open(sinaurls)
print(result.read())