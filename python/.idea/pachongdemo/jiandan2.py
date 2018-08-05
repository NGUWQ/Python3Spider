#Created by TTT
import requests
from bs4 import BeautifulSoup as BS
import re
import urllib.request
import os
import random
#爬取网站图片
def urlmethod(url):
    req=urllib.request.Request(url)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    iplist=['212.8.252.106:1080','101.236.35.98:8866','118.190.95.35:9001','61.135.217.7:80']
    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})#字典类型
    opener=urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
def gettext(url):
    try:
        urlmethod(url)
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def save_imgs(folder='pictures'):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://www.hugsmxy.com/'
    soup = BS(gettext(url), 'html.parser')
    img = (soup.find_all('img', {"src":re.compile('.jpg')}))
    imgurl=list()
    i=0
    for imgs in img:
        imgurl.append(url+(imgs.attrs.get('src')))
        print(i.__str__()+'.jpg')
        imgreq = requests.get(imgurl[i])
        with open(i.__str__()+'.jpg', 'wb') as f:
            f.write(imgreq.content)
        i=i+1
    print("have save")

if __name__=='__main__':
    save_imgs()