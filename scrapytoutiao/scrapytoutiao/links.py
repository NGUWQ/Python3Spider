from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time

browser=webdriver.Chrome()
def getlink():
    """
    拿到每篇文章的链接
    :return:
    """
    url = 'https://www.toutiao.com/ch/nba/'
    browser.get(url)
    # 设置隐式等待，最多等待10s
    browser.implicitly_wait(5)
    # 模拟鼠标拖动
    for x in range(7):
        js = "var q=document.documentElement.scrollTop=" + str(x * 700)
        browser.execute_script(js)
        time.sleep(2)
    time.sleep(5)
    #链接数组
    links=[]
    response = browser.page_source
    soup = BS(response, 'lxml')
    groups = soup.find_all(class_='link')
    for group in groups:
        links.append(group.attrs['href'])
    return links

if __name__ == '__main__':
    print(getlink())
    browser.close()