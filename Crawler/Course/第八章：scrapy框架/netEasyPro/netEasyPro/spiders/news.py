# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from netEasyPro.items import NeteasyproItem
from time import sleep


class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    module_urls = []  # 存储五个板块对应详情页的url

    def __init__(self):
        '''
         创建一个参数对象，用来控制chrome以无界面模式打开
        '''
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        '''
         如何实现让selenium规避被检测到的风险
        '''
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.bro = webdriver.Chrome(executable_path='D:\Google\Chrome\Application/chromedriver.exe', options=option)

    # 处理首页得到模块标题及url
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        demand_list = [3, 4, 6, 7, 8]
        for index in demand_list:
            module = li_list[index].xpath('./a/text()').extract_first()
            module_url = li_list[index].xpath('./a/@href').extract_first()
            print(module, module_url)
            self.module_urls.append(module_url)

            item = NeteasyproItem()
            item['module'] = module

            # 依次对每一个板块对应的页面进行请求
            yield scrapy.Request(url=module_url, callback=self.parse_module, meta={'item': item})

    # 解析每个板块页面中的新闻标题和新闻详情页的url
    def parse_module(self, response):
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            news_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            # print(title, news_detail_url)

            item = response.meta['item']
            item['title'] = title

            yield scrapy.Request(url=news_detail_url, callback=self.parse_news_detail, meta={'item': item})

    # 解析新闻内容
    def parse_news_detail(self, response):
        new_detail = response.xpath('//div[@id="endText"]//text()').extract()
        new_detail = ''.join(new_detail)
        print(new_detail)

        item = response.meta['item']
        item['new_detail'] = new_detail
        # yield item

    def close(spider, reason):
        spider.bro.close()
        print('爬虫结束！')

