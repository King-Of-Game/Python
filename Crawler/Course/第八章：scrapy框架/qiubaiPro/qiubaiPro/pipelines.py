# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class QiubaiproPipeline(object):
    fp = None

    # 重写父类方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫......')
        self.fp = open('./qiubai.txt', 'w', encoding='utf8')

    '''
        # 专门用来处理item类型对象
        # 该方法可以接收爬虫文件提交过来的item对象
        # 该方法每接收到一个item就会被调用一次
    '''
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content + '\n')
        return item  # item对象会传递给下一个即将被执行的管道类

    # 重写父类方法：该方法只在爬虫结束的时候被调用一次
    def close_spider(self, spider):
        print('爬虫完毕！')
        self.fp.close()

# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class mysqlPipeline(object):
    conn = None
    cursor = None  # 游标对象


    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='qiubai', charset='utf8')
        print('开启数据库连接...')


    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        sql = "insert into qiubai values('%s', '%s')" % (item["author"], item["content"])
        try:
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


