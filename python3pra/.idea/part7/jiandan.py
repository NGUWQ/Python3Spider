__author__ = 'WQ'
# *_*coding:utf-8 *_*
#利用selenium模拟浏览器获取煎蛋妹子图片
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup as BS
from hashlib import md5
from multiprocessing.pool import Pool
from urllib.parse import quote
import requests
import os

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Host': 'ww3.sinaimg.cn'
}
#Chrome Headless模式(无界面模式)
chrome_options=webdriver.ChromeOptions()#创建ChromeOptions对象
chrome_options.add_argument('--headless')#添加headless参数
browser=webdriver.Chrome(chrome_options=chrome_options)
wait=WebDriverWait(browser,10)


def getimagesrc(page):
    '''
    根据页码获取图片的url
    :param page: 页码
    '''
    url='http://jandan.net/ooxx/page-'+str(page)+'#comments'
    browser.get(url)
    html=browser.page_source
    #使用beautifulsoup解析
    soup=BS(html,'lxml')
    images=soup.select('img')
    return images
    '''
    #pyquery解析库
    doc=pq(html)
    items=doc('.commentlist .text')
    for item in items.items():
        for i in item.children().items():
            for j in i.children().items():
                if j.attr('src'):
                    print(j.attr('src'))
    '''

def getimage(page,images):
    '''
    下载图片,文件名为每页的页码
    '''
    if not os.path.exists(str(page)):
        os.makedirs(str(page))
    for image in images:
        if image['src'][0:4]=='http':
            imageurl=image['src']
            print(imageurl)
            try:
                response=requests.get(imageurl,headers)
                if response.status_code==200:
                    file_path='{0}/{1}.{2}'.format(str(page),md5(response.content).hexdigest(),'jpg')
                    if not os.path.exists(file_path):
                        with open(file_path,'wb') as f:
                            f.write(response.content)
                    else:
                        print('already downloaded')
            except requests.ConnectionError:
                print('failed downloaded')


start=1
end=2
def main(page):
    images=getimagesrc(page)
    getimage(page,images)



if __name__ == '__main__':
    pool=Pool()
    pages=([x for x in range(start,end+1)])
    pool.map(main,pages)
    pool.close()
    pool.join()
    browser.close()
