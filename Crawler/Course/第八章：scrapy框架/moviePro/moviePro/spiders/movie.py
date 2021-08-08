# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from moviePro.items import MovieproItem
from redis import Redis


class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['wwww.xxx.com']
    start_urls = ['http://ys.okfanhao.com/fhdq_renqi_0_0_1.htm']

    rules = (
        Rule(LinkExtractor(allow=r'fhdq_renqi_0_0_\d+'), callback='parse_item', follow=True),
    )

    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379)

    # 处理番号列表页面数据
    def parse_item(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
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

        item = MovieproItem()
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


