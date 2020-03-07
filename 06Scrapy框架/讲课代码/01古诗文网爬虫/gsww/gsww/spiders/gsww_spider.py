# -*- coding: utf-8 -*-
import scrapy
from ..items import GswwItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import Selector

class GswwSpiderSpider(scrapy.Spider):
    name = 'gsww_spider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org/default_1.aspx']

    def myprint(self,value):
        print("="*30)
        print(value)
        print("="*30)

    def parse(self, response):
        # self.myprint(type(response))
        # respsone.xpath返回的都是SelectorList对象
        # SelectorList：里面存储的都是Selector对象
        # SelectorList.getall：可以直接获取xpath中指定的值。
        # SelectorList.get：可以直接提取第一个值。

        gsw_divs = response.xpath("//div[@class='left']/div[@class='sons']")
        for gsw_div in gsw_divs:
            title = gsw_div.xpath('.//b/text()').get()
            source = gsw_div.xpath(".//p[@class='source']/a/text()").getall()
            dynasty = source[0]
            author = source[1]
            # 下面的//text()代表的是获取class='contson'下的所有子孙文本
            content_list = gsw_div.xpath(".//div[@class='contson']//text()").getall()
            content = "".join(content_list).strip()
            item = GswwItem(title=title,dynasty=dynasty,author=author,content=content)
            yield item

        next_href = response.xpath("//a[@id='amore']/@href").get()
        if next_href:
            next_url = response.urljoin(next_href)
            request = scrapy.Request(next_url)
            yield request
