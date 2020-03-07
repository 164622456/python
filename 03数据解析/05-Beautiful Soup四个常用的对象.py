#--coding:utf-8--

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse">111</p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b><!--Hey, buddy. Want to buy a used parser?--></b>
"""

soup = BeautifulSoup(html, 'lxml')
# print(soup.p)
# print(type(soup.p))
#
# print(soup.p.name)
# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.p.get('class'))

# soup.p['class'] = 'new'
# print(soup.p)


from bs4.element import NavigableString
print(soup.p.string)
print(type(soup.p.string))


print(type(soup))

# from bs4.element import Comment
# print(soup.b.string)
# print(type(soup.b.string))