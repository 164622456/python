import re
import requests

def parse_page(page_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # resp = requests.get(page_url,headers=headers)
    # text = resp.text
    text = ""
    with open("赶集.html",'r',encoding='utf-8') as fp:
        text = fp.read()
    houses = re.findall(r'''
    <div.+?ershoufang-list".+?<dd.*?<a.+?>(.+?)</a>.+? # 标题
    <dd.+?<span>(.+?)</span>.+? # 户型
    <span.+?<span>(.+?)</span>.+? # 面积
    ''',text,re.DOTALL | re.VERBOSE)
    for house in houses:
        print(house)



if __name__ == '__main__':
    base_url = "http://cs.ganji.com/zufang/pn{}/"
    for x in range(1,11):
        page_url = base_url.format(x)
        parse_page(page_url)
        break