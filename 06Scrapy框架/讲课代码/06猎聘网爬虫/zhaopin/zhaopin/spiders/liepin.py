# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders.crawl import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ZhaopinItem

class LiepinSpider(CrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python']

    # https://www.liepin.com/job/1919503055.shtml
    rules = (
        Rule(LinkExtractor(allow=r'https://www.liepin.com/job/\d+\.shtml.*',restrict_xpaths=['//ul[@class="sojob-list"]//a']),callback='parse_job',follow=False),
        Rule(LinkExtractor(allow=r'/zhaopin/.+curPage=\d+',restrict_xpaths=['//div[@class="pagerbar"]//a']),follow=True)
    )

    def parse_job(self, response):
        title = response.css(".title-info h1::text").get()
        company = response.css(".title-info h3 a::text").get()
        city_list = response.css(".basic-infor span::text").getall()
        city = "".join(city_list).strip()
        edu = response.css(".job-qualifications span:nth-child(1)::text").get()
        work = response.css(".job-qualifications span:nth-child(2)::text").get()
        desc_list = response.css(".content-word::text").getall()
        desc = "".join(desc_list).strip()
        item = ZhaopinItem(title=title,company=company,city=city,edu=edu,work=work,desc=desc)
        yield item
