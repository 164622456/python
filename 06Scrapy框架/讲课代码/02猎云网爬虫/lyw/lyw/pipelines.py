# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# twisted
from twisted.enterprise import adbapi

class LywPipeline(object):
    def __init__(self,mysql_config):
        self.dbpool = adbapi.ConnectionPool(
            mysql_config['DRIVER'],
            host=mysql_config['HOST'],
            port=mysql_config['PORT'],
            user=mysql_config['USER'],
            password=mysql_config['PASSWORD'],
            db=mysql_config['DATABASE'],
            charset='utf8'
        )

    @classmethod
    def from_crawler(cls,crawler):
        # 只要重写了from_crawler方法，那么以后创建对象的时候，就会调用这个方法来获取pipline对象
        mysql_config = crawler.settings['MYSQL_CONFIG']
        return cls(mysql_config)

    def process_item(self, item, spider):
        result = self.dbpool.runInteraction(self.insert_item,item)
        result.addErrback(self.insert_error)
        return item

    def insert_item(self,cursor,item):
        sql = "insert into article(id,title,author,pub_time,content,origin) values(null,%s,%s,%s,%s,%s)"
        args = (item['title'],item['author'],item['pub_time'],item['content'],item['origin'])
        cursor.execute(sql,args)

    def insert_error(self,failure):
        print("="*30)
        print(failure)
        print("="*30)

    def close_spider(self,spider):
        self.dbpool.close()

