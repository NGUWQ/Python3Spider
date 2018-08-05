# -*- coding: utf-8 -*-
from scrapy import Spider
from urllib.parse import quote
from scrapysplashtest.items import ProductItem
from scrapy_splash import SplashRequest


script="""
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#mainsrp-pager div.form > input').value=%d;document.querySelector('#mainsrp-pager div.form > span.btn.J_Submit').click()", args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
  end



"""


class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_urls = 'https://s.taobao.com/search?q={}&sort=sale-desc'
    #base_urls = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORD'):
            for page in range(self.settings.get('MAX_PAGE')+1):
                url=self.base_urls.format(quote(keyword))
                #url = self.base_urls+quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='execute',
                                    args={'lua_source': script, 'page': page, 'wait': 7})



    def parse(self, response):
        products=response.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"]//div[contains(@class,"item")]')
        for product in products:
            item=ProductItem()
            item['price']=''.join(product.xpath('.//div[contains(@class,"price")]//text()').extract()).strip()
            item['title']=''.join(product.xpath('.//div[contains(@class,"title")]//text()').extract()).strip()
            item['shop']=''.join(product.xpath('.//div[contains(@class,"shop")]//text()').extract()).strip()
            item['image']=''.join(product.xpath('.//div[@class="pic"]//img[contains(@class,"img")]/@data-src').extract()).strip()
            item['deal']=product.xpath('.//div[contains(@class,"deal-cnt")]//text()').extract_first()
            item['location']=product.xpath('.//div[contains(@class,"location")]//text()').extract_first()
            yield item
