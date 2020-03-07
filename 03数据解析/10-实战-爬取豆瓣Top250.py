#--coding:utf-8--

import requests
from bs4 import BeautifulSoup


headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'Cookie': 'll="108288"; bid=o1ll0wMPfCo; __guid=223695111.3077529162061502500.1578490580383.0073; __utmz=223695111.1578490581.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=W7D36ig5zE8QcIAuwDmh04Qw57MHMcCm; trc_cookie_storage=taboola%2520global%253Auser-id%3D9fd4818a-4586-4156-9a68-a6ee0061a2a0-tuct3a4786c; _vwo_uuid_v2=D90750E455427DE1A4C8BE5A40B9FF016|71daae99d470c1167664378cc67c2dd8; __gads=ID=af6ce2546828f002:T=1581751835:S=ALNI_MaxepEqNLDCTidXyGhCh6qdzl8acA; __utmz=30149280.1582343613.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="61401416:cDXWIWXoHCo"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.6140; douban-profile-remind=1; ck=waiB; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1582953183%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dhn90NBDLR4MfH5T0QDZLi-HiBdVZ5fGaAhtmmA9Qh5yvip6mCcXsjt5GhiXVOrDJE6NJyWVfyufubzx3XQWUEa%26wd%3D%26eqid%3Dcec362a50008afe7000000025e15dacb%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1139372761.1578490581.1582343613.1582953183.4; __utmb=30149280.0.10.1582953183; __utmc=30149280; __utma=223695111.73170899.1578490581.1578490581.1582953183.2; __utmb=223695111.0.10.1582953183; __utmc=223695111; _pk_id.100001.4cf6=7c1817a18ae69633.1578490581.2.1582953763.1578490581.'
}
# 获取详情页面url
def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')

    ol = soup.find('ol', class_='grid_view')
    if  ol != None:
        lis = ol.find_all('li')
    else:
        lis = None

    detail_urls = []
    if  lis != None:
        for li in lis:
            detail_url = li.find('a')['href']
            # print(detail_url)
            detail_urls.append(detail_url)
    return detail_urls
#解析详情页面内容

def parse_detail_url(url,f):
    # 解析详情页面内容
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    # 电影名
    name = list(soup.find('div', id='content').find('h1').stripped_strings)
    name = ''.join(name)
    # print(name)
    # 导演
    director = list(soup.find('div', id='info').find('span').find('span', class_='attrs').stripped_strings)
    # print(director)
    # # 编剧
    # # screenwriter = list(soup.find('div', id='info').find_all('span')[3].find('span', class_='attrs').stripped_strings)
    # # print(screenwriter)
    # # 演员
    # actor = list(soup.find('span', class_='actor').find('span', class_='attrs').stripped_strings)
    # # print(actor)

    # 编剧
    screenwriter_span = soup.find('div', id='info').find_all('span')[3].find('span', class_='attrs')
    # print(screenwriter_span)
    if screenwriter_span != None:
        screenwriter = list(screenwriter_span.stripped_strings)
        screenwriter = ''.join(screenwriter)
        print(screenwriter)
    else:
        screenwriter = '无'
    # 演员
    actor_span = soup.find('span', class_='actor')
    # print(actor_span)
    if actor_span != None:
        actor = list(actor_span.find('span', class_='attrs').stripped_strings)
        actor = ''.join(actor)
        print(actor)
    else:
        actor = '无'


    # 评分
    score = soup.find('strong', class_='ll rating_num').string
    print(url)
    print(score)
    print('*'*30)
    f.write('{},{},{},{},{}\n'.format(name,''.join(director),''.join(screenwriter),''.join(actor),score))

def main():
    base_url = 'https://movie.douban.com/top250?start={}&filter='
    with open('Top250.csv','w',encoding='utf-8') as f:
        for x in range(0,251,25):
            url = base_url.format(x)
            print(url)
            detail_urls = get_detail_urls(url)
            for detail_url in detail_urls:
               parse_detail_url(detail_url,f)

if __name__ == '__main__':
    main()