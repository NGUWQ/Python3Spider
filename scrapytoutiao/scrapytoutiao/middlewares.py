# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
from logging import getLogger


class SeleniumMiddleware():
    def __init__(self,timeout=None,service_args=[]):
        self.logger=getLogger(__name__)
        self.browser=webdriver.PhantomJS(service_args=service_args)
        self.timeout=timeout
        self.wait=WebDriverWait(self.browser,self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self,request,spider):
        """
        用PhantomJS抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        try:
            self.logger.debug('PhantomJS is Starting')
            self.browser.get(request.url)
            return HtmlResponse(url=request.url,body=self.browser.page_source,
                                    request=request,encoding='utf-8',status=200)
            
        except TimeoutException:
            return HtmlResponse(url=request.url,status=500,request=request)



    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
            service_args=crawler.settings.get('SELENIUM_TIMEOUT')
        )

