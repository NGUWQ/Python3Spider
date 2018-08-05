#Created by TTT
import urllib.request
import re
import random
import requests
def daili(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req=urllib.request.Request(url=url,headers=headers)
    iplist=['212.8.252.106:1080','61.135.217.7:80','118.190.95.43:9001','110.72.193.161:8123']
    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
    openner=urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(openner)
    return req

def pachong():
    url='http://www.hugsmxy.com/'
    request=daili(url)
    reponse=urllib.request.urlopen(request)
    content = reponse.read().decode('utf-8')
    pattern = re.compile('.png')
    img=re.findall(pattern,content)
    imgurl=list()
    i=0
    for imgs in img:
        #imgurl.append(url+(imgs.attrs.get('src')))
        #print(i.__str__()+'.jpg')
        #imgreq=requests.get(imgurl[i])
        with open(i.__str__()+'.jpg','w') as f:
            #f.write(imgreq.content)
            f.write(imgs)
        i+=1
        if i>5:
            break
if __name__=='__main__':
    pachong()
