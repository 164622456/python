# -*- coding: utf-8 -*-
import scrapy
from ..items import LjItem
import re
import json
from scrapy_redis.spiders import RedisSpider

class HouseSpider(RedisSpider):
    name = 'house'
    allowed_domains = ['lianjia.com']
    # start_urls = ['https://www.lianjia.com/city/']
    redis_key = 'lj'

    def parse(self, response):
        self.logger.info("="*30)
        city_tags = response.css(".city_list_ul a")
        for city_tag in city_tags:
            city_url = city_tag.css("::attr(href)").get()
            city_name = city_tag.css("::text").get()
            item = LjItem(city=city_name)
            yield scrapy.Request(city_url+"ershoufang/",callback=self.parse_region_list,meta={"item":item})

    def parse_region_list(self,response):
        # 解析行政区的url
        item = response.meta.get('item')
        region_tags = response.css("div[data-role='ershoufang'] .sub_nav a")
        for region_tag in region_tags:
            region_url = region_tag.css("::attr(href)").get()
            region_name = region_tag.css("::text").get()
            item['region'] = region_name
            yield scrapy.Request(response.urljoin(region_url),callback=self.parse_house_page,meta={"item":item})

    def parse_house_page(self,response):
        # 翻页
        page_data = response.css("div[comp-module='page']::attr(page-data)").get()
        totalPage = json.loads(page_data)['totalPage']
        for x in range(1, totalPage + 1):
            yield scrapy.Request(response.url + "pg" + str(x), callback=self.parse_house_list,meta={"item":response.meta.get('item')})


    def parse_house_list(self,response):
        # 解析房源列表
        item = response.meta.get("item")
        detail_urls = response.css(".sellListContent li>a::attr(href)").getall()
        for detail_url in detail_urls:
            result = re.search(r'/ershoufang/\d+\.html',detail_url)
            if result:
                yield scrapy.Request(detail_url,callback=self.parse_house,meta={"item":item})


    def parse_house(self,response):
        # 解析房源详情页
        item = response.meta.get('item')
        item['title'] = response.css("h1.main::text").get()
        item['total_price'] = response.css(".price .total::text").get()
        item['unit_price'] = response.css(".unitPriceValue::text").get()
        item['house_type'] = response.css(".content ul li:nth-child(1)::text").get()
        item['orientation'] = response.css(".content ul li:nth-child(7)::text").get()
        item['full_area'] = response.css(".content ul li:nth-child(3)::text").get()
        item['inside_area'] = response.css(".content ul li:nth-child(5)::text").get()
        item['years'] = response.css(".area .subInfo::text").get()
        yield item










