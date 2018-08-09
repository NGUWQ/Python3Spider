#利用selenium抓取去哪儿酒店数据(可抓全国以及境外所有酒店信息)

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
import time
import csv
import requests
import random
import pymongo


browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
js = "var q=document.documentElement.scrollTop=100000"
mongo_uri='localhost'
mongo_db='qunar'
client=pymongo.MongoClient(mongo_uri)
db=client[mongo_db]
collection='hotel'


def getcities():
    """
    获取去哪儿度假所有城市
    :return: 所有城市生成器
    """
    depurl = 'https://touch.dujia.qunar.com/depCities.qunar'
    response = requests.get(depurl)
    deps = response.json()
    for dep_item in deps['data']:
        for dep in deps['data'][dep_item]:
            yield dep  # 出发城市

def selecthotel():
    """
    获取去哪儿酒店页面详情页
    :return:页面数据
    """
    url = 'http://hotel.qunar.com/'
    browser.get(url)
    '''
    #选取境外酒店
    aboroad_hotel = wait.until(EC.element_to_be_clickable((By.ID, 'js_searchtype_inter')))
    aboroad_hotel.click()
    '''
    #选取酒店类型,在此我们我们默认选择境内酒店,
    #type=wait.until(EC.presence_of_element_located((By.ID,'js_searchtype_inter')))
    tocity=wait.until(EC.presence_of_element_located((By.ID,'toCity')))#目的地
    #页面默认城市为北京，清除即可。
    tocity.clear()
    time.sleep(1)
    tocity.send_keys('深圳')#如选取境外酒店,这里更改城市名称就行
    tocity.send_keys(Keys.ENTER)
    time.sleep(1)
    #tocity_add=wait.until(EC.presence_of_element_located((By.ID,'q')))#选填,可加酒店名,商圈。
    click=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'search-btn')))
    click.click()
    time.sleep(random.uniform(2,3))
    score=browser.find_element_by_id('wrapper_SCORE-desc')#按评分帅选
    score.click()
    time.sleep(random.uniform(2,3))
    page=1
    while page <3:
        browser.execute_script(js)
        time.sleep(7)
        response =browser.page_source
        parse(response)
        time.sleep(2)
        next_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.item.next')))
        next_page.click()
        time.sleep(7)
        page=page+1

def parse(response):
    """
    解析每一页的酒店信息
    :param response: 网页数据
    :return:
    """
    doc=pq(response)
    items=doc('#jxContentPanel .b_result_box').items()
    for item in items:
        hotel= {
            '酒店名':item.find('.e_title.js_list_name').text(),
            '价格': item.find('.js_list_price > p > a > b').text(),
            '评分':item.find('.score').text(),
            '评价':item.find('.review.first_review > a').text(),
            '地址':item.find('.adress > span').text(),
            '点评':item.find('.user_comment > a').text()

        }
        savetomongodb(hotel)
        savetocsv(hotel)
        print(hotel)
    print('保存成功')


def savetomongodb(hotel):
    """
    保存酒店信息到mongodb数据库
    :param hotel: 酒店信息
    :return:
    """
    db[collection].insert(hotel)


def savetocsv(hotel):
    """
    保存到csv文件
    :param hotel: 酒店信息
    :return:
    """
    with open('qunar_routes.csv','a+',newline='',encoding='utf-8') as csvfile:
        fieldnames=['酒店名','价格','评分','评价','地址','点评']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow(hotel)

if __name__ == '__main__':
    """
    若想爬取全国所有城市的酒店信息,将注释去掉后在selecthotel()中传入城市即可
    """
    #cities=getcities()
    selecthotel()
    browser.close()
    client.close()


