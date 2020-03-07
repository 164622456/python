import re

# ^：以...开头：
# text = "hello world"
# result = re.search("world",text)
# print(result.group())


# $：以...结尾：
# text = "hello world"
# result = re.search("hello$",text)
# print(result.group())
# text = ""
# result = re.search("^$",text)
# print(result.group())


# |：匹配多个字符串或者表达式：



# 贪婪和非贪婪：
text = "12345"
result = re.search("\d+?", text)
print(result.group())

result1 = re.search("\d?", text)
print(result1.group())


# 案例1：提取html标签名称：
# text = "<h1>这是标题</h1>"
# result = re.search("<.+?>",text)
# print(result.group())


# 案例2：验证一个字符是不是0-100之间的数字：
# 0,1,99,100
# 01
# text = "101"
# result = re.match("0$|[1-9]\d?$|100$",text)
# print(result.group())











