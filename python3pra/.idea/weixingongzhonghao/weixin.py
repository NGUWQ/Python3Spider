__author__ = 'WQ'
# *_*coding:utf-8 *_*
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup as BS
from lxml import etree
import requests

base_url = 'http://weixin.sogou.com/weixin?type=2&s_from=input&query='
browser=webdriver.Chrome()
keyword = 'NBA'


def getsougouindex():
    start_url = base_url +keyword
    browser.get(start_url)

def getarticlehref():
    response=browser.page_source
    html=etree.HTML(response)
    results=html.xpath('//h3/a/@href')
    for result in results:
        response=requests.get(result)
        doc=etree.HTML(response.text)
        items=doc.xpath('//div[@class="rich_media_content "]/p/text()')
        print(items)
        print('---------------------------')
    '''
    soup=BS(response,'lxml')
    href=soup.find_all('h3 a')
    print(href)
    
    items = doc('.news-box .news-list .txt-box').items()
    for item in items:
        doc=pq(item)
        items=doc('h3').items()
        for item in items:
            print(item)
        
        url = item.attr('href')
        print(url)
        '''



if __name__ == '__main__':
    getsougouindex()
    getarticlehref()