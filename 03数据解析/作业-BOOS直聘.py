#--coding:utf-8--

import requests
from lxml import etree

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    text = resp.text
    html = etree.HTML(text)
    ul = html.xpath("//div[@class='job-list']//ul")[0]
    lis = ul.xpath("./li")
    detail_urls = []
    for li in lis:
        detail_url = li.xpath(".//div[@class='info-primary']/h3/a/@href")
        # print(company_urls)
        detail_url = 'https://www.zhipin.com' + detail_url[0]
        detail_urls.append(detail_url)

    return detail_urls

def parse_detail_url(url,f):
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    text = resp.text
    html = etree.HTML(text)
    # 工作
    job_name = html.xpath("//div[@class='company-info']//div[@class='name']/h1/text()")
    # print(job_name)
    # 工资
    job_pay = html.xpath("//div[@class='company-info']//div[@class='name']/span/text()")
    # print(job_pay)
    # 福利待遇
    job_tags = html.xpath("//div[@class='company-info']//div[@class='job-tags']//span/text()")
    # 职位描述
    job_description = html.xpath("//div[@class='detail-content']/div[@class='job-sec']/div[@class='text']/text()")
    job_description = ''.join(job_description).replace(r'\n','').strip()
    # print(job_description)
    # 公司
    company_name = html.xpath("//div[@class='sider-company']/div[@class='company-info']/a[2]/text()")
    company_name = ''.join(company_name).replace(r'\n', '').strip()
    # print(company_name)
    # 公司信息
    company_info = html.xpath("//div[@class='sider-company']/p/text() | //div[@class='sider-company']/p/a/text()")
    # print(company_info)


    f.write('{},{},{},{},{},{}\n'.format(job_name,job_pay,job_tags,job_description,company_name,company_info))

def main():

    base_url = 'https://www.zhipin.com/c101010100-p100109/?page={}&ka=page-{}'

    with open('boos.csv','a',encoding='utf-8') as f:

        for x in range(1, 11):
            url = base_url.format(x, x)
            detail_urls = get_detail_urls(url)
            for detail_url in detail_urls:
                parse_detail_url(detail_url, f)


if __name__ == '__main__':
    main()
