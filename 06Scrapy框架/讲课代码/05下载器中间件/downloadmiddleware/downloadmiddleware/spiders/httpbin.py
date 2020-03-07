# -*- coding: utf-8 -*-
import scrapy

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        print("="*30)
        print(response.text)
        print("="*30)
        yield scrapy.Request(self.start_urls[0],dont_filter=True)
