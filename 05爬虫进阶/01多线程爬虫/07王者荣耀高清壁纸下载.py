# 获取壁纸的url是：
"""
https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=0&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1554385943910
"""

import threading
import queue
import requests
from urllib import parse
import os
from urllib import request
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer": "https://pvp.qq.com/web201605/wallpaper.shtml"
}


class Producer(threading.Thread):
    """
    用来生成壁纸图片
    """
    def __init__(self, page_queue,image_queue,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.image_queue = image_queue

    @staticmethod
    def extract_images(data):
        images = []
        for x in range(1, 9):
            img_no = "sProdImgNo_%d" % x
            img_url = parse.unquote(data.get(img_no)).replace("200", "0")
            images.append(img_url)
        return images

    def run(self) -> None:
        while not self.page_queue.empty():
            page_url = self.page_queue.get()
            resp = requests.get(page_url, headers=headers)
            datas = resp.json().get("List")
            for data in datas:
                img_urls = Producer.extract_images(data)
                prodname = parse.unquote(data.get("sProdName")).replace("1:1","").strip()
                dir_path = os.path.join("images", prodname)
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                for index, img_url in enumerate(img_urls):
                    self.image_queue.put({"name": prodname, "img_url": img_url, "index": index})
        print("%s线程执行完成"%threading.current_thread().name)



class Consumer(threading.Thread):
    def __init__(self,page_queue,images_queue,lock,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.images_queue = images_queue
        self.lock = lock

    def run(self) -> None:
        while True:
            try:
                image_obj = self.images_queue.get(timeout=60)
                dirname = image_obj.get("name")
                img_url = image_obj.get('img_url')
                index = image_obj.get("index")
                # 如果不存在这个文件夹，就创建一个文件夹
                dir_path = os.path.join("images",dirname)
                # 下载图片了
                try:
                    request.urlretrieve(img_url, os.path.join(dir_path, "%s.jpg" % index))
                    print(os.path.join(dir_path, "%s.jpg" % index) + "下载完成！")
                except Exception as e:
                    print('='*30)
                    print(e)
                    print(img_url)
                    print('=' * 30)
            except queue.Empty as e:
                print(e)
                time.sleep(0.1)
                continue


def main():
    page_queue = queue.Queue(20)
    images_queue = queue.Queue(1000)
    lock = threading.Lock()

    for x in range(0,18):
        page_url = "https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={page}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1554446236641".format(page=x)
        page_queue.put(page_url)

    for x in range(5):
        th = Producer(page_queue,images_queue,name="生产者线程%d"%x)
        th.start()

    for x in range(5):
        th = Consumer(page_queue,images_queue,lock,name="消费者线程%d"%x)
        th.start()


if __name__ == '__main__':
    main()

