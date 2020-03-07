#--coding:utf-8--

from urllib import request

url = 'https://www.zhihu.com/hot'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'cookie':'_zap=59cde9c3-c5c0-4baa-b756-fa16b5e72b10; d_c0="APDi1NJcuQ6PTvP9qa1EKY6nlhVHc_zYWGM=|1545737641"; __gads=ID=237616e597ec37ad:T=1546339385:S=ALNI_Mbo2JturZesh38v7GzEeKjlADtQ5Q; _xsrf=pOd30ApWQ2jihUIfq94gn2UXxc0zEeay; q_c1=1767e338c3ab416692e624763646fc07|1554209209000|1545743740000; tst=h; __utma=51854390.247721793.1554359436.1554359436.1554359436.1; __utmb=51854390.0.10.1554359436; __utmc=51854390; __utmz=51854390.1554359436.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; __utmv=51854390.100-1|2=registration_date=20180515=1^3=entry_date=20180515=1; tgw_l7_route=537a925d07d06cecbf34cd06a153f671; capsion_ticket="2|1:0|10:1554360474|14:capsion_ticket|44:NDM3YzM4ZjY3MjRkNDJhZGE2ZTFlNDgyYjYzYzhkNWM=|4f72c1edb70a779711a93844e747deb0d7efb6febfd6254d11b3a27844c50a00"; z_c0="2|1:0|10:1554360480|4:z_c0|92:Mi4xOWpCeUNRQUFBQUFBOE9MVTBseTVEaVlBQUFCZ0FsVk5vUGFTWFFCRXZ2bkkzTTNRZk9IVU1NOXFMYXdGNFMwTVB3|769f186a095046f171488c3ba61242ff27bcdef068c2d4cafc6046ff008e1a1a"'
}
rq = request.Request(url,headers=headers)
resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))