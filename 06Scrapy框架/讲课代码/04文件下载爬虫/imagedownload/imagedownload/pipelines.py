# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from imagedownload import settings
import os
import re

class ImagedownloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        media_requests = super(ImagedownloadPipeline, self).get_media_requests(item,info)
        for media_request in media_requests:
            media_request.item = item
        return media_requests


    def file_path(self, request, response=None, info=None):
        origin_path = super(ImagedownloadPipeline, self).file_path(request,response,info)
        title = request.item['title']
        title = re.sub(r'[\\/:\*\?"<>\|]',"",title)
        save_path = os.path.join(settings.IMAGES_STORE,title)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        image_name = origin_path.replace("full/","")
        return os.path.join(save_path,image_name)

