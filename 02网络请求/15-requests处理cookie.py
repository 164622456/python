#--coding:utf-8--


import requests

# resp = requests.get('https://www.baidu.com/')
# print(resp.cookies)
# print(resp.cookies.get_dict())


# 案例一
# url = 'https://www.zhihu.com/hot'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#     'cookie':'_zap=59cde9c3-c5c0-4baa-b756-fa16b5e72b10; d_c0="APDi1NJcuQ6PTvP9qa1EKY6nlhVHc_zYWGM=|1545737641"; __gads=ID=237616e597ec37ad:T=1546339385:S=ALNI_Mbo2JturZesh38v7GzEeKjlADtQ5Q; _xsrf=pOd30ApWQ2jihUIfq94gn2UXxc0zEeay; q_c1=1767e338c3ab416692e624763646fc07|1554209209000|1545743740000; tst=h; __utma=51854390.247721793.1554359436.1554359436.1554359436.1; __utmc=51854390; __utmz=51854390.1554359436.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; __utmv=51854390.100-1|2=registration_date=20180515=1^3=entry_date=20180515=1; l_n_c=1; l_cap_id="OWRiYjI0NzJhYzYwNDM3MmE2ZmIxMGIzYmQwYzgzN2I=|1554365239|875ac141458a2ebc478680d99b9219c461947071"; r_cap_id="MmZmNDFkYmIyM2YwNDAxZmJhNWU1NmFjOGRkNDNjYjc=|1554365239|54372ab1797cba8c4dd224ba1845dd7d3f851802"; cap_id="YzQwNGFlYWNmNjY3NDFhNGI4MGMyYjZjYjRhMzQ1ZmE=|1554365239|385cc25e3c4e3b0b68ad5747f623cf3ad2955c9f"; n_c=1; capsion_ticket="2|1:0|10:1554366287|14:capsion_ticket|44:MmE5YzNkYjgzODAyNDgzNzg5MTdjNmE3NjQyODllOGE=|40d3498bedab1b7ba1a247d9fc70dc0e4f9a4f394d095b0992a4c85e32fd29be"; z_c0="2|1:0|10:1554366318|4:z_c0|92:Mi4xOWpCeUNRQUFBQUFBOE9MVTBseTVEaVlBQUFCZ0FsVk5iZzJUWFFEWi1JMkxnQXlVUXh2SlhYb3NmWks3d1VwMXRB|81b45e01da4bc235c2e7e535d580a8cc07679b50dac9e02de2711e66c65460c6"; tgw_l7_route=578107ff0d4b4f191be329db6089ff48'
# }
# resp = requests.get(url,headers=headers)
# print(resp.text)


# 案例二


post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F'

post_data = {
    'username':'1097566154@qq.com',
    'password':'wq15290884759.'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# 登录
session = requests.session()
session.post(post_url,headers=headers,data=post_data)


#访问个人网页
url = 'https://i.meishi.cc/cook.php?id=13686422'

resp = session.get(url)
print(resp.text)