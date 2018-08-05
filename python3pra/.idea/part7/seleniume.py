__author__ = 'WQ'
# *_*coding:utf-8 *_*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()  # 浏览器对象初始化
try:
    browser.get('https://www.cnblogs.com/101718qiong/')  # 请求网页
    input = browser.find_element_by_id('kw')  # 根据id值来获取搜索节点
    input.send_keys('Python')  # 节点交互传入搜索值
    input.send_keys(Keys.ENTER)  # 传入enter键
    wait = WebDriverWait(browser, 10)  # 最长等待时间
    ouput = wait.until(EC.presence_of_element_located((By.ID, 'content_left')))  # 10秒内该id节点是否成功加载出来
    other = wait.until(EC.title_is(u'Silence&QH - 博客园'))
    print(browser.current_url)  # 打印当前url
    print(ouput)
    print(other)
    # print(browser.get_cookies())#daycookies
    # print(browser.page_source)  # 打印源代码
finally:
    browser.close()
