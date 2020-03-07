# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# pip install fake-useragent
from fake_useragent import UserAgent
import random

class UserAgentDownloadMiddleware(object):
    def process_request(self,request,spider):
        ua = UserAgent()
        user_agent_str = ua.random
        # print(user_agent_str)
        request.headers['User-Agent'] = user_agent_str

class IPProxyDownloadMiddleware(object):
    PROXIES = [{"ip":"124.113.192.168","port":4231,"expire_time":"2019-05-09 22:58:55"},{"ip":"117.57.35.70","port":4273,"expire_time":"2019-05-09 22:58:55"}]
    def process_request(self,request,spider):
        proxy = random.choice(self.PROXIES)
        # http://124.113.192.168:4231
        proxy_url = "http://" + proxy['ip'] + ":" + str(proxy['port'])
        request.meta['proxy'] = proxy_url