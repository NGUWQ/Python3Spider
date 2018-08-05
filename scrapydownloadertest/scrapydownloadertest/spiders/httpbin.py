__author__ = 'WQ'
# *_*coding:utf-8 *_*
import scrapy

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains=['httpbin.org']
    start_urls=['http://httpbin.org/get']

    def parse(self, response):
        self.logger.debug(response.text)
        self.logger.debug('status code:'+str(response.status))