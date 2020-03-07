import re
## 匹配单个字符 ##

# *：匹配0个或者多个字符：
text = "+abc"
result = re.match('\D*',text)
print(result.group())


# +：匹配1个或者多个字符：
# text = "1+abc"
# result = re.match('\w+',text)
# print(result.group())


# ?：匹配前一个字符0个或者1个：
# text = "a+bc"
# result = re.match('\w?',text)
# print(result.group())


# {m}：匹配m个字符:
# text = "+1abc"
# result = re.match('\w{2}',text)
# print(result.group())


# {m,n}：匹配m-n之间的个数的字符：
# text = "1abc+"
# result = re.match('\w{1,3}',text)
# print(result.group())
