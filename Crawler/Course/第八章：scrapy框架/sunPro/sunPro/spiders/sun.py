# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem
from sunPro.items import DetailItem


# 需求：爬取小说分类、名称、人气、简介
class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.69shu.org/fenlei/1_1/']

    # 链接提取器：根据指定规则（allow="正则"）进行链接的提取
    link_extractor = LinkExtractor(allow=r'fenlei/1_(?!16|\d{3,})')
    link_detail_extractor = LinkExtractor(allow=r'/book/\d+/(?!\d+\.html)')  # /book/\d+/(?!\d+\.html)
    rules = (
        # 规则解析器：将链接提取器提取到的链接进行指定规则（callback）的解析操作
        # follow=True：可以将链接提取器继续作用到，链接提取器提取的链接，对应的页面中
        Rule(link_extractor, callback='parse_novel_name', follow=False),

        Rule(link_detail_extractor, callback='parse_novel_detail', follow=False),
    )

    '''
    以下两个解析方法没有手动发起请求，是不可以实现请求传参的: 也就是说不能通过yield scrapy.Request() 回调其它函数
    无法将两个解析方法解析的数据存储到同一个item中，可以依次存储到两个item中
    '''
    # 解析小说类别、名称、作者
    def parse_novel_name(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[su@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

        print('\n', response)
        # 注意：xpath表达式中不可以出现tbody标签
        li_list = response.xpath('/html/body/div[3]/div/div/div[2]/div[1]/div[2]/ul/li')
        for li in li_list:
            novel_category = li.xpath('./span[1]/text()').extract_first()
            novel_name = li.xpath('./span[2]/a/text()').extract_first()
            novel_author = li.xpath('./span[4]/text()').extract_first()
            # print(novel_category, novel_name, novel_author)

            item = SunproItem()
            item['novel_category'] = novel_category
            item['novel_name'] = novel_name
            item['novel_author'] = novel_author
            yield item

    # 解析小说人气和简介
    def parse_novel_detail(self, response):
        # print(response)
        novel_popularity = response.xpath('//*[@id="info"]/p/span/text()').extract_first()
        novel_synopsis = response.xpath('//*[@id="info"]/div[3]//text()').extract()
        novel_synopsis = ''.join(novel_synopsis)
        # print(novel_popularity)

        item = DetailItem()
        item['novel_popularity'] = novel_popularity
        item['novel_synopsis'] = novel_synopsis
        yield item
