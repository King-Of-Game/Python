# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem


class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']

    redis_key = 'fbs'
    rules = (
        Rule(LinkExtractor(allow=r'fenlei/1_(?!16|\d{3,})'), callback='parse_item', follow=True),
    )

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

            item = FbsproItem()
            item['novel_category'] = novel_category
            item['novel_name'] = novel_name
            item['novel_author'] = novel_author



