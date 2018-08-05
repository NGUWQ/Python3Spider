# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapychinacom.loaders import ChinaLoader
from scrapychinacom.items import NewsItem

class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles/']

    def parse_item(self, response):
        loader=ChinaLoader(item=NewsItem(),response=response)
        loader.add_xpath('title','//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url',response.url)
        loader.add_xpath('text','//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime','//div[@id="chan_newsInfo"]/text()',re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source','//div[@id="chan_newsInfo"]/text()',re='来源：(.*)')
        loader.add_value('website','中华网')
        yield loader.load_item()
