# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from scrapytoutiao.links import getlink
from scrapytoutiao.items import NBAItem

class ToutiaoSpider(Spider):
    name = 'toutiao'
    allowed_domains = ['www.toutiao.com']
    base_urls = 'https://www.toutiao.com'

    def start_requests(self):
        links=getlink()
        for link in links:
            url=self.base_urls+link
            yield Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        try:
            item=NBAItem()
            item['title']=response.xpath('//div[@class="article-box"]//h1[contains(@class,"article-title")]//text()').extract_first()
            item['source']=response.xpath('//div[@class="article-box"]//div[contains(@class,"article-sub")]//text()').re('[\u4e00-\u9fa5_a-zA-Z]+')[-1]#匹配中文和字母
            item['datetime']=response.xpath('//div[@class="article-box"]//div[contains(@class,"article-sub")]//text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')#匹配时间
            item['content']=''.join(response.xpath('//div[@class="article-box"]//div[contains(@class,"article-content")]//text()').extract()).strip()
            yield item
        except:
            print('与规则不符,抓取失败')
