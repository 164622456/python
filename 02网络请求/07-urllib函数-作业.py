#--coding:utf-8--

from urllib import request

#必做内容

url = 'https://www.biedoul.com/'
resp = request.urlopen(url)

print(resp.read().decode('utf-8'))


#选做内容

for i in range(10229,10232):
    url = 'https://www.biedoul.com/index/'+str(i)
    resp = request.urlopen(url)

    print(resp.read().decode('utf-8'))