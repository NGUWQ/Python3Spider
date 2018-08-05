__author__ = 'WQ'
# *_*coding:utf-8 *_*
#前进和后退
import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.zhihu.com/')
browser.get('https://www.taobao.com/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()