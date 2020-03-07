#--coding:utf-8--

import requests

proxy = {
    'http':'111.77.197.127:9999'
}
url = 'http://www.httpbin.org/ip'
resp = requests.get(url,proxies=proxy)
print(resp.text)