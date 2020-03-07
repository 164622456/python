# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
from .models import ProxyModel
import threading
import time

class IPDownloaderMiddleware(object):
    def __init__(self):
        super(IPDownloaderMiddleware, self).__init__()
        self.current_proxy = None
        self.update_proxy_url = 'http://d.jghttp.golangapi.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
        self.update_proxy()
        self.lock = threading.Lock()
        # 创建一个多线程：专门用来管理代理的
        # 管理方式：只要这个代理的时间超过了1分钟，或者是这个代理被拉黑了，那么在多线程中就要更换代理了
        th = threading.Thread(target=self.update_proxy_in_thread)
        th.start()

    def process_request(self, request, spider):
        # 更换代理，是在请求之前更换，也就是在这个函数中更换的
        request.meta['proxy'] = self.current_proxy.proxy_url

    def process_response(self, request, response, spider):
        # 在响应中，通过判断状态码，来判断是否需要更新代理
        if response.status != 200:
            # 标记某个标记位，要更新代理了
            self.lock.acquire()
            self.current_proxy.is_blacked = True
            self.lock.release()
            # 如果这个请求没有被正确的响应到，那么应该重新返回，等待下一次重新请求获取
            return request
        # 如果是正常的响应，那么一定要记得返回response，否则在爬虫中获取不到
        return response

    def update_proxy(self):
        resp = requests.get(self.update_proxy_url, headers=self.headers)
        proxy_model = ProxyModel(resp.json())
        self.current_proxy = proxy_model
        print("更新了新的代理：%s"%self.current_proxy.proxy_url)


    def update_proxy_in_thread(self):
        # 管理方式：只要这个代理的时间超过了1分钟，或者是这个代理被拉黑了，那么在多线程中就要更换代理了
        count = 0
        while True:
            time.sleep(10)
            if count >= 6 or self.current_proxy.is_blacked:
                self.update_proxy()
                count = 0
            else:
                count += 1
                print("count+1=%d"%count)

