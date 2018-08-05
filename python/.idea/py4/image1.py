#coding=utf-8
import urllib
import re
#py抓取页面图片并保存到本地

#获取页面信息
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

#通过正则获取图片
def getImg(html):
    reg ='.png'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
    #循环把图片存到本地
    x = 0
    for imgurl in imglist:
        #保存到本地
        urllib.urlretrieve(imgurl,'.idea/py2/img/%s.jpg' % x)
        x+=1

html = getHtml("http://www.hugsmxy.com/")
getImg(html)