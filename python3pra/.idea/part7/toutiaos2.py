__author__ = 'WQ'
# *_*coding:utf-8 *_*
#利用selenium模拟浏览器点击操作获取今日头条街拍图片
from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from pyquery import PyQuery as pq
from hashlib import md5
import os
import requests

KEYWORD='街拍'
#Chrome Headless模式(无界面模式)
chrome_options=webdriver.ChromeOptions()#创建ChromeOptions对象
chrome_options.add_argument('--headless')#添加headless参数
browser=webdriver.Chrome(chrome_options=chrome_options)
wait=WebDriverWait(browser,10)

def getpage():
    '''
    抓取结果页
    '''
    browser.get('https://www.toutiao.com/')
    input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#rightModule div.tt-input >input')))
    submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#rightModule div.tt-input button.tt-button >span')))#第一种点击
    submit=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'tt-button')))#第三种点击
    input.clear()
    input.send_keys(quote(KEYWORD))#传入关键词
    #input.send_keys(Keys.ENTER)#第二种点击
    now_handle=browser.current_window_handle#定位到当前页面
    submit.click()#点击确定
    all_handles=browser.window_handles#获得所有页面
    for handle in all_handles:
        if handle!=now_handle:
            browser.switch_to_window(handle)#定位到新页面
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.y-wrap')))#定位到街拍图片信息

def getsource():
    '''
    抓取图片组
    '''
    html=browser.page_source
    doc=pq(html)
    items=doc('.rbox-inner').items()
    for item in items:
        title=pq(item.find('.title-box').text()).text()
        for i in item.find('.img-list').items():
            yield {
                'title':title,
                'group':i.find('.img-wrap ').attr('href')[7:]#街拍组图片
            }

def getgroupimage(image):
    '''
    得到每组图片
    :param image: 每组图片
    '''
    baseurl='https://www.toutiao.com/a'
    browser.get(baseurl+image.get('group'))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.imageList')))
    html=browser.page_source
    doc=pq(html)
    items=doc('.imageList .image-list').items()
    for item in items:
        for i in item.find('.image-item .image-item-inner').items():
            url=i.children().attr('data-src')#得到每张图片的url
            downloadimage(url,image)

def downloadimage(url,image):
    '''
    下载图片并保存到文件夹
    :param url:
    :param items:
    '''
    if not  os.path.exists(image.get('title')):
        os.mkdir(image.get('title'))
    try:
        response=requests.get(url)
        if response.status_code==200:
            file_path='{0}/{1}.{2}'.format(image.get('title'),md5(response.content).hexdigest(),'.jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
        else:
            print('already downloaded')
    except requests.ConnectionError:
        print('failed to save image')


def main():
    getpage()
    items=getsource()
    for item in items:
        getgroupimage(item)
    browser.close()


if __name__ == '__main__':
    main()
