#--coding:utf-8--


from urllib import parse

url = 'http://www.baidu.com/index.html;user?id=S#comment'

result = parse.urlparse(url)
# result = parse.urlsplit(url)

print(result)
print(result.scheme)
print(result.netloc)
print(result.path)
print(result.params)
