# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SunproPipeline(object):
    def process_item(self, item, spider):
        '''
            将数据写入数据库时，如何保证数据的一致性?
            如果两个item类可以爬到相同的id，那就根据id插入数据，
            如果不行，那就用一个item类型，spider使用scrapy.Request(meta={'item':item})传参
        '''

        # 判定处理不同的 item对象
        if item.__class__.__name__ == 'DetailItem':
            novel_popularity = item['novel_popularity']
            novel_synopsis = item['novel_synopsis']
            print(novel_popularity)
        else:
            novel_category = item['novel_category']
            novel_name = item['novel_name']
            novel_author = item['novel_author']
            print(novel_category, novel_name, novel_author)
        return item
