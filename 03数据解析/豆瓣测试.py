import requests
from bs4 import BeautifulSoup

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'https://movie.douban.com/subject/26430107/'
# 解析详情页面内容
resp = requests.get(url, headers=headers)
# print(resp.text)
html = resp.text
soup = BeautifulSoup(html, 'lxml')
# 电影名
name = list(soup.find('div', id='content').find('h1').stripped_strings)
name = ''.join(name)
print(name)
# 导演
director = list(soup.find('div', id='info').find('span', class_ = 'attrs').stripped_strings)
director = ''.join(director)
print(director)
# 编剧
screenwriter_span = soup.find('div', id='info').find_all('span')[3].find('span', class_ = 'attrs')
# print(screenwriter_span)
if  screenwriter_span != None:
    screenwriter = list(screenwriter_span.stripped_strings)
    screenwriter = ''.join(screenwriter)
    print(screenwriter)
else:
    screenwriter = '无'
# 演员
actor_span = soup.find('span', class_='actor')
print(actor_span)
if  actor_span != None:
    actor = list(actor_span.find('span', class_='attrs').stripped_strings)
    actor = ''.join(actor)
    print(actor)
else:
    actor = '无'
# 评分
score = soup.find('strong', class_='ll rating_num').string
print(score)

str = '{},{},{},{},{}\n'.format(name,''.join(director),''.join(screenwriter),''.join(actor),score)
print(str)