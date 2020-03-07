# -*- coding: utf-8 -*-
import scrapy


class GswwSpiderSpider(scrapy.Spider):
    name = 'gsww_spider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['http://gushiwen.org/']

    def parse(self, response):
        pass
