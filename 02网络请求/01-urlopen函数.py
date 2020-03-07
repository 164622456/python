#--coding:utf-8--

from urllib import request

resp = request.urlopen('https://www.sogou.com/')

print(resp.getcode())