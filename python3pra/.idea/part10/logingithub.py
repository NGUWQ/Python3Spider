__author__ = 'WQ'
# *_*coding:utf-8 *_*
import requests
from lxml import etree
from bs4 import BeautifulSoup as BS
from pyquery import PyQuery as pq

class Login(object):

    def __init__(self):
        self.headers={
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url='https://github.com/login'
        self.post_url='https://github.com/session'
        self.logined_url='https://github.com/settings/profile'
        self.session=requests.session()
        self.user='NGUWQ'
        self.password='Wq1996122421'

    def token(self):
        response=self.session.get(self.login_url,headers=self.headers)
        selector=etree.HTML(response.text)
        token=selector.xpath('//div//input[2]/@value')#//div/form/input[3]/@value
        return token

    def login(self):
        form_data={
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token':self.token()[0],
            'login': self.user,
            'password':self.password
        }

        response=self.session.post(self.post_url,data=form_data,headers=self.headers)
        if response.status_code==200:
            self.dynamics(response.text)
            print('true')

        response=self.session.get(self.logined_url,headers=self.headers)
        if response.status_code==200:
            self.profile(response.text)
            print('true')




    def dynamics(self,html):
        '''
        doc=pq(html)
        items=doc('.two-thirds')
        print(items)

        soup=BS(html,'lxml')
        print(soup.select('.d-flex >div'))
        
        selector=etree.HTML(html)
        dynamics=selector.xpath('//div[contains(@class, "news")]')
        for dynamic in dynamics:
            print(dynamic)
        '''
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamic = ' '.join(item.xpath(' ')).strip()
            print(dynamic)


    def profile(self,html):
        selector=etree.HTML(html)
        name=selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email=selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name,email)


if __name__ == '__main__':
    login=Login()
    login.login()