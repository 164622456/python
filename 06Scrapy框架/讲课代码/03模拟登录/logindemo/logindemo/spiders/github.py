# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").get()
        # formdata = {
        #     "commit": "Sign in",
        #     "utf8": "✓",
        #     "authenticity_token": authenticity_token,
        #     "login": "hynever@163.com",
        #     "password": "pythonspider123",
        #     "webauthn-support": "supported"
        # }
        # yield scrapy.FormRequest("https://github.com/session",formdata=formdata,callback=self.after_login)
        yield scrapy.FormRequest.from_response(response,formdata={
            "login": "hynever@163.com",
            "password": "pythonspider123"
        },callback=self.after_login)


    def after_login(self,response):
        yield scrapy.Request("https://github.com/settings/profile",callback=self.visit_profile)


    def visit_profile(self,response):
        with open("github_profile.html",'w',encoding='utf-8') as fp:
            fp.write(response.text)
