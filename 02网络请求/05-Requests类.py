#--coding:utf-8--

from urllib import request

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
rq = request.Request('https://www.baidu.com/',headers=header)

resp = request.urlopen(rq)
print(resp.read())