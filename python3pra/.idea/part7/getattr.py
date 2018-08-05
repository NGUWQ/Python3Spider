__author__ = 'WQ'
# *_*coding:utf-8 *_*
#获取属性
from selenium import webdriver
from  selenium.webdriver import ActionChains
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
logo=browser.find_element_by_id('zh-top-link-logo')
input=browser.find_element_by_class_name('zu-top-link-logo')
print(logo)
print(logo.get_attribute('class'))#获取当前节点属性
print(logo.text)#获取当前节点文本
print(input.id)#获取节点id
print(input.location)#获取该节点在页面中的相对位置
print(input.tag_name)#获取标签名称
print(input.size)#获取节点的大小