import re

## 匹配单个字符 ##

# 匹配某个字符串：
# text = "abc"
# ret = re.match('a', text)
# print(ret.group())


# 点（.）：匹配任意的字符(除了'\n')：
text = "\nabc"
ret = re.match('.',text)
print(ret.group())


# \d：匹配任意的数字：
# text = "aab"
# ret = re.match('\d',text)
# print(ret.group())


# \D：匹配任意的非数字：
# text = "cab"
# ret = re.match('\D',text)
# print(ret.group())


# \s：匹配的是空白字符（包括：\n，\t，\r和空格）：
# text = " ab"
# ret = re.match('\s',text)
# print("="*30)
# print(ret.group())
# print("="*30)


# \S：非空白字符：
# text = "\nab"
# ret = re.match('\S',text)
# print("="*30)
# print(ret.group())
# print("="*30)


# \w：匹配的是a-z和A-Z以及数字和下划线：
# text = "+bc"
# ret = re.match('\w',text)
# print("="*30)
# print(ret.group())
# print("="*30)


# \W：匹配的是和\w相反的：
# text = "1bc"
# ret = re.match('\W',text)
# print("="*30)
# print(ret.group())
# print("="*30)


# []组合的方式，只要满足中括号中的某一项都算匹配成功：
# text = "bc"
# ret = re.match('[1b]',text)
# print("="*30)
# print(ret.group())
# print("="*30)

# 使用组合的方式[0-9]\d：
# text = "abc"
# ret = re.match('[^0-9]',text)
# print("="*30)
# print(ret.group())
# print("="*30)

# 使用组合的方式实现\w：
# text = "+bc"
# ret = re.match('[^a-zA-Z0-9_]',text)
# print("="*30)
# print(ret.group())
# print("="*30)



