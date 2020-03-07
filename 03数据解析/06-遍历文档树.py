#--coding:utf-8--

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b>
<!--Hey, buddy. Want to buy a used parser?-->
</b>
"""

soup = BeautifulSoup(html,'lxml')

# head_tag = soup.head
# print(head_tag.contents)
# print(head_tag.children)
# for i in head_tag.children:
#     print(i)

# for string in soup.strings:
#     print(repr(string))


# for string in soup.stripped_strings:
#     print(repr(string))


# print(soup.b.strings)