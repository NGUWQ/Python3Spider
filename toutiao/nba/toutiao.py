from selenium import webdriver
from bs4 import BeautifulSoup as BS
from nba.config import *
import time
import pymongo
#利用selenium爬取今日头条(ajax异步加载)

#Chrome Headless模式(无界面模式)
chrome_options=webdriver.ChromeOptions()#创建ChromeOptions对象
chrome_options.add_argument('--headless')#添加headless参数
browser=webdriver.Chrome(chrome_options=chrome_options)

client=pymongo.MongoClient(MONGO_URI)
db=client[MONGO_DB]
collection='nba'

def getlink():
    """
    拿到每篇文章的链接
    :return:
    """
    url = 'https://www.toutiao.com/ch/nba/'
    browser.get(url)
    # 设置隐式等待，最多等待10s
    browser.implicitly_wait(5)
    # 模拟鼠标拖动
    for x in range(5):
        js = "var q=document.documentElement.scrollTop=" + str(x * 700)
        browser.execute_script(js)
        time.sleep(2)
    time.sleep(5)
    #链接数组
    links=[]
    response = browser.page_source
    #browser.close()
    soup = BS(response, 'lxml')
    groups = soup.find_all(class_='link')
    for group in groups:
        links.append(BASE_URL+group.attrs['href'])
    return links

def getnews(links):
    """
    获取每篇新闻
    :param links: 链接列表
    :return:
    """
    for link in links:
        browser.get(link)
        html=browser.page_source
        soup=BS(html,'lxml')
        sources=[]
        content=''
        if soup.find(class_='article-sub'):
            for each in soup.find(class_='article-sub'):
                if each.string.strip():
                    sources.append(each.string.strip())
            for each in soup.find(class_='article-content').find(name='p'):
                if each.string:
                    content=''.join(each.string)
            yield {
                'tittle':soup.find(class_='article-title').string,
                'source':sources[0],
                'datetime':sources[1],
                'content':content
            }
        else:
            continue


def savemongodb(new):
    """
    保存到mongodb数据库
    :param new: 新闻
    :return:
    """
    db[collection].insert(dict(new))

if __name__ == '__main__':
    links=getlink()
    items=getnews(links)
    for item in items:
        savemongodb(item)
    client.close()
    browser.close()







