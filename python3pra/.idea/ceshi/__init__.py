__author__ = 'WQ'
# *_*coding:utf-8 *_*
from selenium import webdriver

browser=webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)