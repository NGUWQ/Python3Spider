__author__ = 'WQ'
# *_*coding:utf-8 *_*
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

#chrome_options=webdriver.ChromeOptions()#创建ChromeOptions对象
#chrome_options.add_argument('--headless')#添加headless参数
browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
KEYWORD='街拍'
browser.get('https://www.toutiao.com/')
input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#rightModule div.tt-input >input')))
submit=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'tt-button')))#第一种点击
input.clear()
input.send_keys(quote(KEYWORD))#传入关键词
#input.send_keys(Keys.ENTER)#第二种点击
now_handle=browser.current_window_handle#定位到当前页面
submit.click()#点击确定
'''
baseurl='https://www.toutiao.com/a'
browser.get(baseurl+'6580500676835541511/')
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.imageList')))
html=browser.page_source
doc=pq(html)
items=doc('.imageList .image-list').items()
for item in items:
   for i in item.find('.image-item .image-item-inner').items():
      print(i.children().attr('data-src'))
'''