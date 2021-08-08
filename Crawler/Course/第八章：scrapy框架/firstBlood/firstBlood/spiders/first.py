# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称：就是爬虫源文件的一个唯一标识
    name = 'first'
    # 允许的域名：用来限定start_urls列表中哪些url可以进行请求发送
    # allowed_domains = ['www.badu.com']    # 一般情况下不用（比如：爬取网站中的图片，图片的url不一定和该网站归属同一域名）

    # 起始的url列表：该列表中存放的url会被scrapy自动进行请求发送
    start_urls = ['https://www.baidu.com/', 'https://www.sogou.com/']

    # 用作数据解析：response参数表示的就是请求成功后对应的响应对象
    def parse(self, response):  # parse()方法被调用的次数 = start_urls列表中的元素个数
        print(response)
