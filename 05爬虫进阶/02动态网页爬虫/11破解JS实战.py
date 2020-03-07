import requests
import time
import random
import hashlib

def main():
    word = input("请输入需要翻译的单词：")
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Referer": "http://fanyi.youdao.com/?keyfrom=fanyi-new.logo",
        "Cookie": "OUTFOX_SEARCH_USER_ID=2083709438@42.48.76.78; OUTFOX_SEARCH_USER_ID_NCOO=1220380506.7194781; JSESSIONID=aaaZw21e6HFsR66SS7BOw; ___rl__test__cookies=1555249298611",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com"
    }
    timestamp = time.time()*1000
    salt = str(timestamp) + str(random.randint(0,10))
    temp = "fanyideskweb" + word + salt + "@6f#X3=cCuncYssPsuRUE"
    sign = hashlib.md5(temp.encode("utf-8")).hexdigest()
    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": timestamp,
        "bv": "94d71a52069585850d26a662e1bcef22",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    resp = requests.post(url,headers=headers,data=data)
    print(resp.json()["translateResult"][0][0]["tgt"])

if __name__ == '__main__':
    main()