# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GswwItem(scrapy.Item):
    title = scrapy.Field()
    dynasty = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
