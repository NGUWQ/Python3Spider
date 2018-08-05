__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
import re
from requests.exceptions import RequestException
import json


def getonepage(url):
    try:
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/'
        }
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parseonepage(html):
    pattern=re.compile('<li>.*?pic.*?em class="">(.*?)</em>.*?<img.*?src="(.*?)".*?title.*?>'
                       +'(.*?)</span>.*?v:average.*?>(.*?)</span>.*?inq.*?>(.*?)</span>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            '排名':item[0],
            '图片链接':item[1],
            '片名':item[2],
            '评分':item[3],
            '评价':item[4]
        }

def writefile(content):
    with open('豆瓣电影top250.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offet):
    url='https://movie.douban.com/top250?start='+str(offet)+'&filter='
    html=getonepage(url)
    items=parseonepage(html)
    for item in items:
        print(item)
        writefile(item)
if __name__ == '__main__':
    for i in range(10):
        main(offet=i*25)