# 1. 因为用户名和密码和验证码的name都是随机的，所以我们要先获取网页源代码，然后提取出其中的name值。
# 2. 获取到了name和once的值以后，再通过调用https://www.v2ex.html/sigin接口，把数据通过post请求发送过去
# 3. 还需要使用云打码平台去自动识别验证码。

import requests
from lxml import etree
from urllib import request
from yundama import YDMHttp

login_url = "https://www.v2ex.com/signin"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "referer": "https://www.v2ex.com/signin",
    'cookie': '_ga=GA1.2.573178911.1553924072; PB3_SESSION="2|1:0|10:1555559114|11:PB3_SESSION|36:djJleDo0Mi40OC43Ni4yMTM6MTQ3MzgwMzM=|eba48e24c9d3ff99c29a06a42537b1a14ecc33d5ed037c6b3e8bfe992529e20d"; V2EX_LANG=zhcn; _gid=GA1.2.1416334932.1555559116; V2EX_TAB="2|1:0|10:1555568644|8:V2EX_TAB|8:dGVjaA==|663a2d344c625d0bfd6197c3f81ff556ba3985aa6a24073fc8af3050ceeb5a35"; V2EX_REFERRER="2|1:0|10:1555579428|13:V2EX_REFERRER|12:RGV2aWxUZWU=|4c07ebf6eb0d40d9712dc8e62d18e59564172caaac8d59a3e38e9c5951356705"'
}

session = requests.Session()
resp = session.get(login_url,headers=headers)
html = resp.text
parser = etree.HTML(html)
inputs = parser.xpath("//form[@action='/signin']//input")
userInput = inputs[0]
passwordInput = inputs[1]
captchaInput = inputs[2]
onceInput = inputs[3]

userName = userInput.get('name')
passwordName = passwordInput.get('name')
captchaName = captchaInput.get('name')
onceValue = onceInput.get('value')

data = {
    userName: 'hyever',
    passwordName: 'abcabc',
    "once": onceValue,
    'next': '/'
}

captcha_url = "https://www.v2ex.com/_captcha?once="+onceValue
imgResp = session.get(captcha_url,headers=headers)
with open("captcha.png",'wb') as fp:
    fp.write(imgResp.content)

ydm = YDMHttp("zhiliao","abcabc")
_,result = ydm.recognize_captcha('captcha.png','3000')
print(result)





