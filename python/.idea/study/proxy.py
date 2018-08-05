#Created by TTT
#代理(隐藏)
import urllib.request
import random
url='https://www.whatismyip.com'
iplist=['212.8.252.106:1080']
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})#字典类型
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('user-agent','Mozilla/5.0 (Windows NT 10.0; WOW64)'
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')]
reponse=urllib.request.urlopen(url)
html=reponse.read().decode('utf-8')
print(html)