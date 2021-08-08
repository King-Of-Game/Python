# -*- coding: utf-8 -*-
import scrapy
from yixuan.items import YixuanItem


class CrawlNovelSpider(scrapy.Spider):
    name = 'crawl_novel'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.69shu.org/top/allvisit/1.html']

    page = 1
    new_url = 'https://www.69shu.org/top/allvisit/%d.html'

    def parse(self, response):
        tr_list = response.xpath('//*[@id="centerl"]/div/div[2]/table/tr')
        count = 0
        for tr in tr_list:
            count += 1
            if count >= 2:
                novel_name = tr.xpath('./td[1]/a/text()')[0].extract()
                novel_author = tr.xpath('./td[3]/a/text()').extract_first()

                item = YixuanItem()
                item["novel_name"] = novel_name
                item["novel_author"] = novel_author
                item["page_num"] = self.page

                detail_url = tr.xpath('./td[1]/a/@href').extract_first()
                # print(f"小说名：{novel_name}, 作者：{novel_author}, url: {detail_url}")
                yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        if self.page < 100:
            self.page += 1
            new_url = format(self.new_url % self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        novel_classification = response.xpath('//*[@id="box-info"]/div[1]/a[2]/text()').extract_first()
        novel_popularity = response.xpath('//*[@id="info"]/p/span/text()').extract_first()[3:-2]

        item = response.meta['item']
        item['novel_classification'] = novel_classification
        item['novel_popularity'] = novel_popularity
        yield item

        print(f"分类: {item['novel_classification']} | 小说名: {item['novel_name']} | 作者: {item['novel_author']} | 人气: {novel_popularity}")
