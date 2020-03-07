import requests
import re

def parse_page(page_url):
    print(page_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    resp = requests.get(page_url,headers=headers)
    text = resp.text
    houses = re.findall(r"""
        <div.+?ershoufang-list".+?<a.+?js-title.+?>(.+?)</a> # 获取房源的标题
        .+?<dd.+?dd-item.+?<span>(.+?)</span> # 获取房源的户型     
        .+?<span.+?<span>(.+?)</span> # 获取房源的面积             
        .+?<div.+?price.+?<span.+?>(.+?)</span> # 获取房源的价格   
    """,text,re.VERBOSE|re.DOTALL)
    for house in houses:
        print(house)

def main():
    base_url = "http://cs.ganji.com/zufang/pn{}/"
    for x in range(1,11):
        page_url = base_url.format(x)
        parse_page(page_url)
        break

if __name__ == '__main__':
    main()


# 总结：
# 1. 如果想要让.代表所有的字符，那么需要在函数后面加re.DOTALL来表示，否则不会代表\n，也就是换行。
# 2. 获取数据的时候，都要用非贪婪模式.
# 3. 如果正则写得不对，那么获取不到结果，程序会假死，这时候可以把你刚刚写的正则删掉，重新运行下，看下程序还会不会假死
# 如果不会假死了，说明正则写得有问题，这是就要去调整了。
# 4. 如果正则写的有问题，那么不要去钻牛角尖，去更换一个思路就可以了。










