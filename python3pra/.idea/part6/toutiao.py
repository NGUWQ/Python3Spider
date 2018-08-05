__author__ = 'WQ'
# *_*coding:utf-8 *_*
#从头条抓取街拍图片(利用Ajax和xhr分析)

import requests
import os
from  hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Host': 'www.toutiao.com',
    'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'X-Requested-With': 'XMLHttpRequest'
}
def get_page(offset):
    params={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab'
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('title'):
                title=item.get('title')
            if item.get('image_list'):
                images=item.get('image_list')
                for image in images:
                    yield {
                        'image':image.get('url'),
                        'title':title
                    }


def saveimage(image):
    if not os.path.exists(image.get('title')):
        os.mkdir(image.get('title'))
    try:
        response=requests.get('http:'+image.get('image'))
        if response.status_code==200:
            file_path='{0}/{1}.{2}'.format(image.get('title'),md5(response.content).hexdigest(),'jpg')#图片名字用图片的MD5加密替代
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('already downloaded',file_path)
    except requests.ConnectionError:
        print('failed to save image')


def main(offset):
    json=get_page(offset)
    get_images(json)
    for item in get_images(json):
        print(item)
        saveimage(item)
Group_START=0#街拍偏移量
Group_END=0

if __name__ == '__main__':
    pool=Pool()
    groups=([x*20 for x in range(Group_END,Group_END+1)])
    pool.map(main,groups)#第一个参数是函数,第二个参数是迭代器,依次将数值传入main中
    pool.close()#关闭进程池,不在接收新的进程
    pool.join()#主进程阻塞,等待子进程的退出
