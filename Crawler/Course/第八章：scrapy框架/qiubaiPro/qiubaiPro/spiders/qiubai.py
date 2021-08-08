# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     # 解析：作者的名称 + 段子内容
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []  # 存储所有解析到的数据
    #     for div in div_list:
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         # extract()可以将Selector对象中data参数存储的字符串提取出来
    #         # author_name = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         author_name = div.xpath('./div[1]/a[2]/h2/text()').extract_first()  # 如果列表中只有一个元素可以用该方法
    #         # 如果列表调用了extract之后，则表示将列表中每一个Selector对象data对应的字符串提取出来
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         dic = {
    #             'author': author_name,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #
    #     return all_data

    # 基于管道
    def parse(self, response):
        # 解析：作者的名称 + 段子内容
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []  # 存储所有解析到的数据
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract()可以将Selector对象中data参数存储的字符串提取出来
            # author_name = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span[2]/h2/text()').extract_first()  # 如果列表中只有一个元素可以用该方法
            # 如果列表调用了extract之后，则表示将列表中每一个Selector对象data对应的字符串提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item  # 将item提交给了管道

# 如果有两个管道类，那item提交给哪个呢？
    # 给优先级最高的那个
