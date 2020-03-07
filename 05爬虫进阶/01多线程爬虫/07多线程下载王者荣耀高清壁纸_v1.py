
# 1. 通过https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=4&totalpage=0&page=0&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17106944943383705404_1554454074902&iAMSActivityId=51991&_everyRead=true&iTypeId=1&iFlowId=267733&iActId=2735&iModuleId=2735&_=1554454074918
# 可以获取到高清壁纸的url
# 2. 获取到高清壁纸的url后，通过parse.unquote可以进行解码，然后将最后的200变成0，就可以得到真实的高清壁纸的图片了
# 3. 获取图片的url的地址中有一个page参数，通过修改page的值，可以进行翻页。默认page是从0开始的。
# 4. page最多只有18页，因此区间是[0,17]。


import requests
from urllib import parse
from urllib import request
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer": "https://pvp.qq.com/web201605/wallpaper.shtml"
}

def extract_images(data):
    image_urls = []
    for x in range(1,9):
        image_url = parse.unquote(data['sProdImgNo_%d'%x]).replace("200", "0")
        image_urls.append(image_url)
    return image_urls



def main():
    page_url = "https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=0&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1554457680964"
    resp = requests.get(page_url,headers=headers)
    result = resp.json()
    datas = result['List']
    for data in datas:
        image_urls = extract_images(data)
        name = parse.unquote(data['sProdName']).replace("1:1","").strip()
        dirpath = os.path.join("images1",name)
        # images1/猪八戒-年年有余
        os.mkdir(dirpath)
        for index,image_url in enumerate(image_urls):
            request.urlretrieve(image_url,os.path.join(dirpath,"%d.jpg"%(index+1)))
            print("%s下载完成！"%(image_url))





if __name__ == '__main__':
    main()
