# -*- coding: utf-8 -*-
import scrapy



class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    # 生成一个通用的url模板（模板是不可变的）
    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2

    def parse(self, response):
        name_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li/a[2]/text()').extract()
        print(name_list)
        # for name in name_list:
        #     print(name)

        if self.page_num <= 11:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动请求发送：callback回调函数是专门用于数据解析
            # return 或 yield使得parse()方法具有返回值，scrapy会根据返回值进行递归调用parse()方法
            yield scrapy.Request(url=new_url, callback=self.parse)