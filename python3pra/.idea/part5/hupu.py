__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
import pyquery
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def getonepage(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': 'https://nba.hupu.com/'
        }
        html=requests.get(url,headers=headers)
        if html.status_code==200:
            return html.text
        return None
    except RequestException:
        return None

def parseonepage(html):
    #BeautifulSoup方式解析
    '''
    soup=BeautifulSoup(html,'lxml')
    for item in soup.select('h4'):
        print(item.get_text())
    '''


    items = soup.find_all('h4')
    for item in items:
        for i in item.find_all('a'):
            print(i.string)



    '''
    pquery方式解析
    doc=pyquery.PyQuery(html)
    items=doc('.news-list').items()
    
    for item in items:
        news=item.find('h4').text()
    for new in news.split(' '):
        with open('虎扑新闻.txt','a',encoding='utf-8') as f:
            f.write('\n'+new+'\n')
    '''

def main():
    url='https://voice.hupu.com/nba'
    html=getonepage(url)
    parseonepage(html)

if __name__ == '__main__':
    main()

