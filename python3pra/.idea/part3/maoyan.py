__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
import re
import json
import time
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from multiprocessing import Pool
def get_one_page(url,offset):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': 'http://maoyan.com/board/4?offset=' + str(offset),
            'Host': 'maoyan.com'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)'
                       +'</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)'
                       +'</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'tittle':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def write_to_file(content):
    with open('猫眼电影top100.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url,offset)
    #soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    #print(soup)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    #单线程抓取(有序)
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
    '''
    #多线程抓取(无序)
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
    '''