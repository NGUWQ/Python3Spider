# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class DoubanItem(Item):
    collection='review'
    user=Field()
    title=Field()
    datetime=Field()
    tag=Field()
    content=Field()

