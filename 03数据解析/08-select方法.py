#--coding:utf-8--
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

# （1）通过标签名查找：
# print(soup.select('a'))
# （2）通过类名查找：
# print(soup.select('.sister'))
# （3）通过id查找：
# print(soup.select('#link1'))
# （4）组合查找：
# print(soup.select('p #link1'))
# print(soup.select('head > title'))
# （5）通过属性查找：
# print(soup.select('a[href="http://example.com/elsie"]'))
# （6）获取内容：
print(soup.select('title')[0].get_text())