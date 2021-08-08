# -*- coding: utf-8 -*-
import scrapy

from redis import Redis
from serialNumber.items import SerialnumberItem


class FhkSpider(scrapy.Spider):
    name = 'fhk'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://ys.okfanhao.com/fhdq_renqi_0_0_1.htm']

    url = 'http://ys.okfanhao.com/fhdq_renqi_0_0_%d.html'
    page_num = 1
    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379)

    def parse(self, response):
        print(response)
        li_list = response.xpath('//article[@class="bd"]/ul/li')
        # print(li_list)
        for li in li_list:
            movie_name = li.xpath('./div/h3/a/text()').extract_first()
            # movie_ticket = li.xpath('./div/h3/span/b/text()').extract_first()
            # 获取详情页的url
            detail_url = 'http://ys.okfanhao.com/' + li.xpath('./div/h3/a/@href').extract_first()
            # 将详情页的url存入redis的set中
            ex = self.conn.sadd('urls', detail_url)
            if ex == 1:
                print('%s没有被爬取过，存入redis数据库中并爬取其对应的详细信息' % detail_url)
                yield scrapy.Request(url=detail_url, callback=self.parse_detail)
            else:
                print('%s: 该影片早已收录在库，无需再爬!' % movie_name)

        # 分页
        if self.page_num <= 400:
            self.page_num += 1
            url = format(self.url % self.page_num)
            print(self.page_num)
            print(url)
            return scrapy.Request(url=url, callback=self.parse)

    # 处理每个番号详细数据
    def parse_detail(self, response):
        serial_number = response.xpath('//div[@class="col-md-6 infos"]/h2/text()').extract_first()
        video_name = serial_number
        author_name = response.xpath('//div[@class="col-md-6 infos"]/h4[2]/a/text()').extract()
        author_name = author_name[0] if len(author_name) == 1 else ','.join(author_name)
        video_tag = response.xpath('//div[@class="col-md-6 infos"]/h4[3]/a/text()').extract()
        video_tag = video_tag[0] if len(video_tag) == 1 else ','.join(video_tag)
        publish_date = response.xpath('//div[@class="col-md-6 infos"]/h4[1]/a/text()').extract_first()
        video_ticket = response.xpath('//div[@class="col-md-6 infos"]/p/span/b/text()').extract_first()

        print(serial_number, author_name, video_tag, video_ticket, publish_date)

        item = SerialnumberItem()
        item['serial_number'] = serial_number
        item['video_name'] = video_name
        item['author_name'] = author_name
        item['video_tag'] = video_tag
        item['publish_date'] = publish_date
        item['video_ticket'] = video_ticket
        yield item

    def close(spider, reason):
        spider.conn.close()
        print('爬虫结束，redis链接关闭！')
