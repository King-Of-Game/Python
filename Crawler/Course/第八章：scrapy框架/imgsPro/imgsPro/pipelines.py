# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

# class ImgsproPipeline(object):
#     def process_item(self, item, spider):
#         return item


class ImgsPipeline(ImagesPipeline):
    # 根据图片地址进行图片二进制数据的请求
    def get_media_requests(self, item, info):
        src = item['src']
        yield scrapy.Request(url=src, meta={'item': item})

    # 指定图片存储路径
    def file_path(self, request, response=None, info=None):
        # imgName = request.url.split('/')[-1]

        item = request.meta['item']
        file_format = item['src'].split('.')[-1]
        imgName = item['imgName']
        path = '%s.%s' % (imgName, file_format)

        return path

    def item_completed(self, results, item, info):
        # 返回给下一个即将被执行的管道类
        return item
