__author__ = 'WQ'
# *_*coding:utf-8 *_*
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient
import requests
client=MongoClient()
db=client['weibo']
collection=db['weibo']
base_url='https://m.weibo.cn/api/container/getIndex?'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/5838108650',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(page):
    params={
        'type':'uid',
        'value':'5838108650',
        'containerid':'1076035838108650',
        'page':page
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('erron',e.args)

def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item=item.get('mblog')
            weibo={}
            weibo['id']=item.get('id')
            weibo['发布时间']=item.get('created_at')
            weibo['内容']=pq(item.get('text')).text()
            weibo['赞']=item.get('attitudes_count')
            weibo['评论数']=item.get('comments_count')
            weibo['转发']=item.get('reposts_count')
            yield weibo


def save_to_mongo(result):
    if collection.insert(result):
        print('saved to mongo')


def main():
    for page in range(1,10):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)

if __name__ == '__main__':
    main()