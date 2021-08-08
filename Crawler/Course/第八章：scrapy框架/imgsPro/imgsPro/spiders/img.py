# -*- coding: utf-8 -*-
import scrapy
from imgsPro.items import ImgsproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        # print(div_list)
        num = 1
        for div in div_list:
            # 注意：图片懒加载要使用其伪属性
            src = 'https:' + div.xpath('./div/a/img/@src2')[0].extract()
            imgName = div.xpath('./div/a/@alt')[0].extract()

            print('正在爬取%s: %s' % (imgName, src))

            item = ImgsproItem()
            item['src'] = src
            item['imgName'] = imgName
            yield item

            if num == 3:
                break
            num += 1

    def close(spider, reason):
        print('爬虫结束！')



