__author__ = 'WQ'
# *_*coding:utf-8 *_*
#执行JavaScript模拟下拉进度条
from selenium import webdriver
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Buttom")')