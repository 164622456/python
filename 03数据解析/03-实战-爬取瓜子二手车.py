#--coding:utf-8--

import requests
from lxml import etree

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'Cookie': 'uuid=5bce551b-ff63-4162-c0bf-c900910d1b34; clueSourceCode=%2A%2300; user_city_id=12; ganji_uuid=7804814600346946730618; sessionid=bf979dc3-7aab-46af-f58b-716d08eac622; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%225bce551b-ff63-4162-c0bf-c900910d1b34%22%2C%22ca_city%22%3A%22bj%22%2C%22sessionid%22%3A%22bf979dc3-7aab-46af-f58b-716d08eac622%22%7D; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A83877503275%7D; cityDomain=bj; antipas=YLcfa7607665B13915bZ90763; preTime=%7B%22last%22%3A1582812492%2C%22this%22%3A1582729907%2C%22pre%22%3A1582729907%7D'
}
#获取详情页面url
def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('utf-8')
    html = etree.HTML(text)
    ul = html.xpath('//ul[@class="carlist clearfix js-top"]')[0]
    # print(ul)
    lis = ul.xpath('./li')
    detail_urls = []
    for li in lis:
        detail_url = li.xpath('./a/@href')
        detail_url = 'https://www.guazi.com' + detail_url[0]
        # print(detail_url)
        detail_urls.append(detail_url)
    return detail_urls

#解析详情页面内容
def parse_detail_page(url):
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('utf-8')
    html = etree.HTML(text)
    title = html.xpath('//div[@class="product-textbox"]/h2/text()')[0]
    title = title.replace(r'\r\n', '').strip()
    # print(title)
    info = html.xpath('//div[@class="product-textbox"]/ul/li/span/text()')
    # print(info)

    price = html.xpath('//span[@class ="pricestype"]/text()')[0]
    price = price.replace(r'¥', '').strip()

    infos = {}
    cardtime = info[0]
    km = info[1]
    displacement = info[2]
    speedbox = info[3]

    infos['title'] = title
    infos['cardtime'] = cardtime
    infos['km'] = km
    infos['displacement'] = displacement
    infos['speedbox'] = speedbox
    infos['price'] = price
    return infos

#保存数据
def save_data(infos,f):

    f.write('{},{},{},{},{},{}\n'.format(infos['title'],infos['cardtime'],infos['km'],infos['displacement'],infos['speedbox'],infos['price']))


def main():
    #第一个url
    base_url = 'https://www.guazi.com/bj/buy/o{}/'
    with open('guazi_bj.csv', 'a', encoding='utf-8') as f:

        for x in range(1, 50):
            url = base_url.format(x)
            #获取详情页面url
            detail_urls = get_detail_urls(url)
            #解析详情页面内容
            for detail_url in detail_urls:
                infos = parse_detail_page(detail_url)
                save_data(infos, f)

if __name__ == '__main__':
    main()




