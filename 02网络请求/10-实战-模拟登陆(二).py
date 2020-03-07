#--coding:utf-8--

from urllib import request
from urllib import parse
from http.cookiejar import  CookieJar

# 登录：https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F
#个人网页https://i.meishi.cc/cook.php?id=13686422

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

#1.登录
#1.1 创建cookiejar对象
cookiejar = CookieJar()
#1.2 使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
#1.3 使用上一步的创建的handler创建一个opener
opener = request.build_opener(handler)
#1.4 使用opener发送登录请求  (账号和密码)

post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F'
post_data = parse.urlencode({
    'username':'1097566154@qq.com',
    'password':'wq15290884759.'
})
req = request.Request(post_url,data=post_data.encode('utf-8'))
opener.open(req)


#2.访问个人网页
url = 'https://i.meishi.cc/cook.php?id=13686422'
rq = request.Request(url,headers=headers)
resp = opener.open(rq)
print(resp.read().decode('utf-8'))