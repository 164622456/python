#--coding:utf-8--

import requests
from bs4 import BeautifulSoup
import time
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

class IpSpider:

    def __init__(self):
        # 1. 准备需要爬取的页面的url
        self.page_urls = []
        for x in range(1, 10):
            page_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(x)
            self.page_urls.append(page_url)

    def parse_page_urls(self,page_url):
        resp = requests.get(page_url, headers=headers)
        # print(resp.text)
        print(resp)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.find('tbody').find_all('tr')
        print(trs)
        infos = []
        for tr in trs:
            info = list(tr.stripped_strings)
            print(info)
            infos.append(info)
        return infos

    def run(self):
        with open("ip.csv", 'w', encoding='utf-8') as fp:
            fp.write('{},{},{},{},{},{},{}\n'.format('IP', 'PORT', '匿名度', '类型', '位置', '响应速度', '最后验证时间'))
            for page_url in self.page_urls:
                # 1. 爬取所有的页面的url
                print(page_url)
                time.sleep(1)
                infos = self.parse_page_urls(page_url)
                for info in infos:
                    fp.write('{},{},{},{},{},{},{}\n'.format(info[0], info[1], info[2], info[3], info[4], info[5], info[6]))


def main():
    spider = IpSpider()
    spider.run()


if __name__ == '__main__':
    main()