from yundama import YDMHttp

ydm = YDMHttp(username='zhiliao',password='abcabc')
uid = ydm.login()
if not uid:
    print("登录失败！")

balance = ydm.balance()
if balance < 10:
    print("余额不足！")

_,result = ydm.decode(filename='image.jpg',codetype="3004")
print(result)

