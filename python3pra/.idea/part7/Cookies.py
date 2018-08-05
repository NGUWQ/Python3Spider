__author__ = 'WQ'
# *_*coding:utf-8 *_*
#selenium的cookies操作
from selenium import webdriver
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name':'wang','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())