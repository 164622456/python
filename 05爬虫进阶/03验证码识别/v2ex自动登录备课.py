
import requests
from lxml import etree
from urllib import request
from yundama import YDMHttp

# 263cf3ef05698b48d6a1544f22055ff505901db6b06a0f6f191ddbcd21cf15fd: hynever
# ab28db3092e67b65d43457bdd5fe0344e87787fb10f887f96be07c7938f14f6c: abcabc
# e28dcaf8f1395fd3e0fc44761e147ba7e961e558ca3ababd4de009075b6381dd: zpeli
# once: 76559
# next: /

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "referer": "https://www.v2ex.com/"
}

def login_v2ex():
    login_url = 'https://www.v2ex.com/signin'
    session = requests.Session()
    resp = session.get(login_url,headers=headers)
    html = resp.text
    with open("login.html",'w',encoding='utf-8') as fp:
        fp.write(html)
    parser = etree.HTML(html)
    inputs = parser.xpath("//form[@action='/signin']//input")
    userInput = inputs[0]
    passwordInput = inputs[1]
    captchaInput = inputs[2]
    onceInput = inputs[3]

    userName = userInput.get("name")
    passwordName = passwordInput.get('name')
    captchaName = captchaInput.get('name')
    onceValue = onceInput.get("value")

    captchaUrl = "https://www.v2ex.com/_captcha?once="+onceValue
    imgResp = session.get(captchaUrl, headers=headers)
    if imgResp.status_code == 200:
        with open("captcha.png", 'wb') as fp:
            fp.write(imgResp.content)
    captchaValue = input("请输入验证码：")
    # while True:
    #     imgResp = session.get(captchaUrl, headers=headers)
    #     if imgResp.status_code == 200:
    #         with open("captcha.png", 'wb') as fp:
    #             fp.write(imgResp.content)
    #     ydm = YDMHttp(username="zhiliao", password="abcabc")
    #     ydm.login()
    #     _, captchaValue = ydm.decode('captcha.png', '3007')
    #     if captchaValue.isalpha():
    #         print(captchaValue)
    #         print("="*30)
    #         break

    data = {
        userName: "hynever",
        passwordName: "abcabc",
        captchaName: captchaValue,
        'once': onceValue,
        'next': '/'
    }
    print(data)
    headers['referer'] = "https://www.v2ex.com/signin"
    session.post(login_url,data=data,headers=headers)
    settingsResp = session.get("https://www.v2ex.com/settings",headers=headers)
    print(settingsResp.text)



if __name__ == '__main__':
    login_v2ex()
