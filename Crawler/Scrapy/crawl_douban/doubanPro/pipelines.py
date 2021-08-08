# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DoubanproPipeline(object):
    def process_item(self, item, spider):
        return item

#　连接my sql 的管道
class MysqlPipeline(object):
    conn = None
    cursor = None  # 游标对象

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='yixuan', charset='utf8')
        print('开启数据库连接...')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        sql = "insert into douban_filmdetail values('%s', '%s', '%s', '%s', '%s', '%s','%s');" \
              % (item['film_id'], item['film_title'], item['film_rate'], item['positive_emotion'], item['negative_emotion'], item['total_score'], item['film_result'], )

        try:
            # print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        film_review_list = item['film_review'].split(';')
        film_review_user_list = item['film_review_user'].split(';')
        film_review_up_list = item['film_review_up'].split(';')
        film_review_date_list = item['film_review_date'].split(';')

        for i in range(len(film_review_list)):
            sql = "insert into douban_filmreview(film_id, film_review, film_review_up, film_review_user, film_review_date) " \
                  "values('%s', '%s', '%s', '%s', '%s');" \
                  % (item['film_id'], film_review_list[i], film_review_up_list[i], film_review_user_list[i], film_review_date_list[i])
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
