# -*- coding: utf-8 -*-
import scrapy
import json
import pandas
import jieba
import wordcloud
from doubanPro.items import DoubanproItem


# 生成词云图片
def getWordCloud(words, film_id):

    new_words_list = []  # 用于存储过滤掉单字词的词汇列表
    # 遍历原始词汇列表
    for word in words:
        if len(word) == 1:
            # 如果是单字词，就跳过这一个继续判定下一个
            continue  # 跳过当前单字词就不会执行下条语句
        # 将非单字词汇添加到该列表
        new_words_list.append(word)

    text = " ".join(new_words_list)  # 用空格把分好的词汇拼接成字符串。示例：'词汇1 词汇2 xxx3....'
    w = wordcloud.WordCloud(font_path='msyh.ttc', width=800, height=400, background_color='white')  # 参数依次为：字体文件，图片宽、高，图片背景颜色
    w.generate(text)  # 开始生成词云数据...
    file_path = 'imgs/'  # 图片存放文件路径
    file_name = '%s.png' % film_id  # 图片名称
    w.to_file(file_path + file_name)  # 生成图片


# 基于波森情感词典计算情感值
def getScore(text, film_id):
    df = pandas.read_table(r"BosonNLP_sentiment_score.txt", sep=" ", names=['key', 'score'])
    key = df['key'].values.tolist()
    score = df['score'].values.tolist()
    # jieba分词
    words = jieba.lcut(text, cut_all=False)  # 返回分词后的list列表
    getWordCloud(words, film_id)  # 调用生成词云的方法

    positive_emotion = 0  # 积极的情感词个数
    negative_emotion = 0  # 消极的情感词个数

    for word in words:
        # 将分词中的词汇和情感词典中的词汇逐个比对
        if word in key:
            # 如果情感得分大于0.6，则判断为积极因素
            if score[key.index(word)] > 0.6:
                positive_emotion += 1
            elif score[key.index(word)] < -0.6:
                negative_emotion += 1

    # 计算情感得分
    score_list = [score[key.index(x)] for x in words if(x in key)]

    dict1 = {
        'positive_emotion': positive_emotion,
        'negative_emotion': negative_emotion,
        'total_score': sum(score_list)
    }

    return dict1


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0']
    # 电影列表url模板
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=%s'
    # 电影对应评论url模板
    comment_url = 'https://movie.douban.com/subject/%s/comments'
    page = 1

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    # 处理页面数据
    def parse(self, response):
        print('\n', response)
        # print(response.text)
        json_data = json.loads(response.text)
        # print(json_data)
        film_list = json_data['subjects']

        for film in film_list:

            film_id = film['id']
            film_title = film['title']
            film_rate = film['rate']
            # print(film_id, film_title, film_rate)

            item = DoubanproItem()
            item['film_id'] = film_id
            item['film_title'] = film_title
            item['film_rate'] = film_rate
            rate = float(film_rate)
            if rate >= 9.5:
                item['film_result'] = '不看后悔'
            elif 9 <= rate < 9.5:
                item['film_result'] = '强烈推荐'
            elif 8 <= rate < 9:
                item['film_result'] = '值得一看'
            elif 7 <= rate < 8:
                item['film_result'] = '一般'
            elif 6 <= rate < 7:
                item['film_result'] = '勉强及格'
            else:
                item['film_result'] = '不及格烂片'

            comment_url = format(self.comment_url % film_id)
            headers = {
                'referer': 'https://movie.douban.com/subject/%s/' % film_id
            }
            yield scrapy.Request(url=comment_url, headers=headers, callback=self.parse_comment, meta={'item': item})

        # 分页:爬取前 x 页
        if self.page < 9:
            self.page = self.page + 1

            url = format(self.url % ((self.page-1)*20))
            yield scrapy.Request(url=url, callback=self.parse)

    # 处理短评页面
    def parse_comment(self, response):
        index = 1  # 只保留前6条评论

        film_review_list = []
        film_review_up_list = []
        film_review_user_list = []
        film_review_date_list = []

        div_list = response.xpath('//*[@id="comments"]/div')
        for div in div_list:
            film_review = div.xpath('./div[2]/p/span/text()').extract_first()
            film_review_up = div.xpath('./div[2]/h3/span[1]/span/text()').extract_first()
            film_review_user = div.xpath('./div[2]/h3/span[2]/a/text()').extract_first()
            film_review_date = div.xpath('./div[2]/h3/span[2]/span[3]/@title').extract_first()[0:10]

            film_review_list.append(film_review)
            film_review_up_list.append(film_review_up)
            film_review_user_list.append(film_review_user)
            film_review_date_list.append(film_review_date)

            index += 1
            # 只保留前6条评论
            if index > 6:
                break

        film_review = ';'.join(film_review_list)
        film_review_up = ';'.join(film_review_up_list)
        film_review_user = ';'.join(film_review_user_list)
        film_review_date = ';'.join(film_review_date_list)

        item = response.meta['item']
        emotion_json = getScore(film_review, item['film_id'])
        positive_emotion = emotion_json['positive_emotion']
        negative_emotion = emotion_json['negative_emotion']
        total_score = emotion_json['total_score']

        item['film_review'] = film_review
        item['film_review_up'] = film_review_up
        item['film_review_user'] = film_review_user
        item['film_review_date'] = film_review_date
        item['positive_emotion'] = positive_emotion
        item['negative_emotion'] = negative_emotion
        item['total_score'] = total_score
        yield item

        # print(item)



