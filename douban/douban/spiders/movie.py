# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from douban.items import DoubanItem


class MovieSpider(Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    base_url = 'https://movie.douban.com/review/best/?start='

    def start_requests(self):
        for start in range(0,self.settings.get('PAGE')):
            url=self.base_url+str(start*20)
            yield Request(url=url,callback=self.parse,dont_filter=True)



    def parse(self, response):
        #reviews=response.xpath('.//div[contains(@class,"review-list chart)"]//div')
        reviews = response.xpath('.//div[contains(@class,"review-list")]//div[@class="main review-item"]')

        item = DoubanItem()
        for review in reviews:
            #print(review)
            #item['user']=review.xpath('.//div[contains(@class,"main review-item")]//a[@class="name"]//text()').extract_first()
            item['user'] = review.xpath('.//a[@class="name"]//text()').extract_first()
            #item['datetime']=review.xpath('.//div[contains(@class,"main review-item")]//span[@class="main-meta"]//text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')#匹配时间
            item['title']=review.xpath('./a/img/@title').extract_first()
            item['datetime'] = review.xpath('.//span[@class="main-meta"]//text()').re_first(
                '(\d+-\d+-\d+\s\d+:\d+:\d+)')  # 匹配时间
            item['tag']=review.xpath('.//div[contains(@class,"main-bd")]/h2/a/text()').extract_first()
            #item['content']=''.join(review.xpath('./div[@class="main-bd"]//div[@class="short-content"]/text()').extract()).strip()
            item['content'] = ''.join(review.xpath('./div[@class="main-bd"]//div[@class="short-content"]/text()').re('[\u4e00-\u9fa5\S]+'))
            yield item
