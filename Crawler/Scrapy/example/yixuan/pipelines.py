# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class YixuanPipeline(object):
    def process_item(self, item, spider):
        return item


class NovelMySqlPipeline(object):
    conn = None
    cursor = None  # 游标对象

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='yixuan',
                                    charset='utf8')
        print('开启数据库连接...')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        sql = """
        insert into novels(novel_classification, novel_name, novel_author, novel_popularity, page_num)
        value ('%s', '%s', '%s', %s, %s)
        
        """ % (item['novel_classification'], item['novel_name'], item['novel_author'],
               item['novel_popularity'], item['page_num'])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(f'执行 SQL 错误：{e}')
            self.conn.rollback()
        return item  # item对象会传递给下一个管道类

    def close_spider(self, spider):
        # self.cursor.close()
        self.conn.close()
        print('数据保存完毕，关闭数据库连接！')
