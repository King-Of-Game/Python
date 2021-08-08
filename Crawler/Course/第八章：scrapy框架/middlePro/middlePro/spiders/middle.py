# -*- coding: utf-8 -*-
import scrapy


class MiddleSpider(scrapy.Spider):
    # 爬取百度
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/s?ie=UTF-8&wd=ip']

    def parse(self, response):
        page_text = response.text
        with open('ip.html', 'w', encoding='utf8') as fp:
            fp.write(page_text)
