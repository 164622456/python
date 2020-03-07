#--coding:utf-8--

from urllib import request
from http.cookiejar import MozillaCookieJar

# 保存
# cookiejar = MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
# resp = opener.open('http://www.httpbin.org/cookies/set/course/abc')
#
# cookiejar.save(ignore_discard=True)  # 即将到期或者已经到期cookie  仍然写入

# ignore_discard=True  即使cookies即将被丢弃也要保存下来
# ignore_expires=True  如果cookies已经过期也将它保存并且文件已存在时将覆盖


#加载

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load()  #即将到期或者已经到期cookie  仍然写入
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://www.httpbin.org/cookies/set/course/abc')

for cookie in cookiejar:
    print(cookie)
