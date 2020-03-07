# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagedownloadItem(scrapy.Item):
    title = scrapy.Field()
    # image_urls：是用来保存这个item上的图片的链接的
    image_urls = scrapy.Field()
    # images：是后期图片下载完成后形成image对象再保存到这个上面
    images = scrapy.Field()
