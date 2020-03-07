#--coding:utf-8--

from urllib import parse

data = {'name':'老王','age':18,'greet':'hello world'}

qs = parse.urlencode(data)
print(qs)

print(parse.parse_qs(qs))


#例子：

from urllib import request

data1 = {'wd':'石原里美'}
qs1 = parse.urlencode(data1)
print(qs1)


url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&'+qs

resp = request.urlopen(url)

# print(resp.read())


# 补充

a = '15290884759'
b = parse.quote(a)
print(b)