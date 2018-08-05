__author__ = 'WQ'
# *_*coding:utf-8 *_*
from selenium import webdriver

proxy='119.23.64.49:3128'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy)
browser=webdriver.Chrome(chrome_options=chrome_options)
#browser.get('http://httpbin.org/get')
browser.get('https://www.baidu.com')