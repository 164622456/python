#--coding:utf-8--

import requests

url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
data = {
    'redirect': 'https://www.meishij.net/',
    'username': '1097566154@qq.com',
    'password': 'wq15290884759.'
}
resp = requests.post(url,headers=headers,data=data)
print(resp.text)