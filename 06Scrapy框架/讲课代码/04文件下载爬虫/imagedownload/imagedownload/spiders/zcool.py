# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders.crawl import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ImagedownloadItem

class ZcoolSpider(CrawlSpider):
    name = 'zcool'
    allowed_domains = ['zcool.com.cn']
    # start_urls = ['http://zcool.com.cn/']
    start_urls = ['https://www.zcool.com.cn/discover/0!0!0!0!0!!!!2!0!1']

    rules = (
        # 翻页的url
        Rule(LinkExtractor(allow=r".+0!0!0!0!0!!!!2!0!\d+"),follow=True),
        # 详情页面的url
        Rule(LinkExtractor(allow=r".+/work/.+html"),follow=False,callback="parse_detail")
    )

    def parse_detail(self, response):
        image_urls = response.xpath("//div[@class='work-show-box']//img/@src").getall()
        title_list = response.xpath("//div[@class='details-contitle-box']/h2/text()").getall()
        title = "".join(title_list).strip()
        item = ImagedownloadItem(title=title,image_urls=image_urls)
        yield item
