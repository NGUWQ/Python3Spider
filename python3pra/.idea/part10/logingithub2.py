__author__ = 'WQ'
# *_*coding:utf-8 *_*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

url='https://github.com/login'
githubu='NGUWQ'
githubp='Wq1996122421'
browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)

browser.get(url)
username=browser.find_element_by_id('login_field')
username.send_keys(githubu)
password=browser.find_element_by_id('password')
password.send_keys(githubp)
submit=wait.until(EC.element_to_be_clickable((By.NAME,'commit')))
submit.click()
html=browser.page_source
doc=pq(html)
items=doc('.news .d-flex .flex-items-baseline').items()
for item in items:
    print(item)
