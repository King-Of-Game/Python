# -*- coding: utf-8 -*-
import scrapy
import time
from bossPro.items import BossproItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c101280100/?query=python&ka=sel-city-101280100']

    url = 'https://www.zhipin.com/c101280100/?query=python&page=%d&ka=page-%d'
    page_num = 1

    def get_header(self):
        referer = format(self.url % (self.page_num, self.page_num))
        header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'lastCity=100010000; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1605344272,1605414348,1605433881,1605440586; __fid=359feb99a2ef63e117a2126787aea581; ___gtid=-247494185; __c=1605414348; __l=l=%2Fwww.zhipin.com%2Fc101280100%2F%3Fquery%3Dpython%26ka%3Dsel-city-101280100&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DmkG6TaIYhZqKYru9oMLuXPdyRsIBURWndpRcpgHf5Xj0VS5D7mOpqOPD6t0BnXvP%26wd%3D%26eqid%3D8923a17000007108000000065fb11446&g=&friend_source=0&friend_source=0; __a=71300573.1605328514.1605328514.1605414348.67.2.34.67; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1605444311; __zp_stoken__=af16bYXhuUQxmO1cAZV1ZRDkvdQd6IFsBKCQ0MSV0XmlkDXMQKG16AHIabUE5Jil0FyB%2BDD10GG9rH3ZmBlwzDEZZFGgpF1Y0fjxkdC0sFFRVbA5BDlxvRFR0GmA7KllIEXF0H3gAFxtIPGAFdA%3D%3D',
            'referer': referer
        }
        return header





    def start_requests(self):
        url = format(self.url % (self.page_num, self.page_num))
        print('正在爬取：%s' % url)

        header = self.get_header()
        yield scrapy.Request(url=url, headers=header, callback=self.parse)

    def parse(self, response):

        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('.//span[@class="job-name"]/a/text()').extract_first()
            job_area = li.xpath('.//span[@class="job-area"]/text()').extract_first()
            detail_url = 'https://www.zhipin.com' + li.xpath('.//span[@class="job-name"]/a/@href').extract_first()

            # print(job_name, job_area)
            item['job_name'] = job_name
            item['job_area'] = job_area

            # 对详情页发请求获取详情页的源码数据
            # 手动请求的发送
            # 请求传参: meta={}, 可以将meta子弹传递给请求对应的回调函数
            header = self.get_header()
            yield scrapy.Request(url=detail_url, headers=header, callback=self.parse_detail, meta={'item': item})

        # 分页操作
        if self.page_num < 2:
            self.page_num += 1
            new_url = format(self.url % (self.page_num, self.page_num))
            print('正在爬取:%s' % new_url)
            time.sleep(5)

            header = self.get_header()
            yield scrapy.Request(url=new_url, headers=header, callback=self.parse)

    # 自定义回调函数: 解析详情页岗位描述
    def parse_detail(self, response):
        job_detail = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_detail = ''.join(job_detail)

        item = response.meta['item']
        item['job_detail'] = job_detail
        yield item


    def close(spider, reason):
        print('爬虫结束')
