__author__ = 'WQ'
# *_*coding:utf-8 *_*
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
input=browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(2)
input.clear()
input.send_keys('ipad')
#button=browser.find_element_by_class_name('btn-search')
#button=browser.find_element_by_css_selector('.btn-search')#css选择器获取
button=browser.find_element_by_xpath('//div[@class="search-button"]/button')#xpath获取
button.click()
'''
#lis=browser.find_elements_by_css_selector('.service-bd li')css选择器获取多个节点
#lis=browser.find_elements_by_xpath('//ul[@class="service-bd"]//li')#xpath获取多个节点
print(lis)
browser.close()
'''