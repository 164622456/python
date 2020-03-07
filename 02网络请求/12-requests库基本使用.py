#--coding:utf-8--


import requests


# 添加headers和查询参数
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
kw = {'wd':'中国'}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get('https://www.baidu.com/s',headers=headers,params=kw)
print(response)


# 属性

# 查询响应内容
# print(response.text)  #返回unicode格式的数据
#
# print(response.content) #返回字节流数据

print(response.url)
print(response.encoding)