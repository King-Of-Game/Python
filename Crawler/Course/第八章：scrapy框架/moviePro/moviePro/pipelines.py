# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class MovieproPipeline(object):
    # conn = None
    #
    # def open_spider(self, spider):
    #     self.conn = spider.conn

    def process_item(self, item, spider):
        dic = {
            'movie_name': item['movie_name'],
            'movie_performer': item['movie_performer'],
            'movie_tag': item['movie_tag'],
            'movie_ticket': item['movie_ticket'],
        }
        print(dic)
        spider.conn.lpush('movieData', str(dic))
        return item


class MysqlPipeline(object):
    conn = None
    cursor = None  # 游标对象

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='yixuan', charset='utf8')
        print('开启数据库连接...')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        sql = "insert into serialnumber_serialnumber(serial_number, video_name, author_name, video_tag, publish_date, video_ticket) " \
              "values('%s', '%s', '%s', '%s', '%s', '%s');" \
              % (item["serial_number"], item["video_name"], item["author_name"], item["video_tag"], item["publish_date"], item["video_ticket"])
        try:
            # print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item  # item对象会传递给下一个管道类

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print('数据保存完毕，关闭数据库连接！')


