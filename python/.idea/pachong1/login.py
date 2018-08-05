#Created by TTT
import urllib.request
import urllib.parse
values={'username':'18872738629','password':'wq1996122418'}
data=urllib.parse.urlencode(values).encode('utf-8')
url='https://weibo.com/login.php'
request=urllib.request.Request(url,data)
response=urllib.request.urlopen(request)
print(response.read())