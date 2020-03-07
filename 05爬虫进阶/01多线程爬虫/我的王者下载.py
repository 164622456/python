import requests
from urllib import request
import threading
import queue
from urllib import parse
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer": "https://pvp.qq.com/web201605/wallpaper.shtml"
}

class Producer(threading.Thread): #获取每个page中，的所有壁纸下的，所有尺寸图片的url与名称
    def __init__(self,page_queue,image_queue,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.image_queue = image_queue

    def run(self) -> None:
        folderpath = "images1"

        while not self.page_queue.empty():
            page_url = self.page_queue.get()
            resp = requests.get(page_url, headers=headers)
            result = resp.json()
            datas = result['List']
            for data in datas:
                image_urls = extract_images(data)
                name = parse.unquote(data['sProdName']).replace("1:1", "").strip()
                dir_path = os.path.join(folderpath, name)
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                for index, image_url in enumerate(image_urls):
                    self.image_queue.put(
                        {"image_url": image_url, "image_path": os.path.join(dir_path, "%d.jpg" % (index + 1))})


class Consumer(threading.Thread):
    def __init__(self,image_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.image_queue = image_queue

    def run(self) -> None:
        while True:
            try:
                image_obj = self.image_queue.get(timeout=10)
                image_url = image_obj.get("image_url")
                image_path = image_obj.get("image_path")
                try:
                    request.urlretrieve(image_url, image_path)
                    print(image_path + "下载完成！")
                except:
                    print(image_path+"下载失败！")
            except:
                break


def extract_images(data):
    image_urls = []
    for x in range(1,9):
        image_url = parse.unquote(data['sProdImgNo_%d'%x]).replace("200", "0")
        image_urls.append(image_url)
    return image_urls

def main():
    page_queue = queue.Queue(18)
    image_queue = queue.Queue(1000)
    for x in range(0, 18):
        page_url = "https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=11&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1583240586638"
        page_queue.put(page_url)

    for x in range(3):
        th = Producer(page_queue,image_queue,name="生产者%d号"%x)
        th.start()

    for x in range(5):
        th = Consumer(image_queue,name="消费者%d号"%x)
        th.start()

if __name__ == '__main__':
    main()