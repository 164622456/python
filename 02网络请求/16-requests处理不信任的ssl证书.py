#--coding:utf-8--


import requests

url = 'https://inv-veri.chinatax.gov.cn/'
resp = requests.get(url,verify = False)

print(resp.content.decode('utf-8'))