# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_id = scrapy.Field()
    film_title = scrapy.Field()
    film_rate = scrapy.Field()
    film_review = scrapy.Field()
    film_review_up = scrapy.Field()
    film_review_user = scrapy.Field()
    film_review_date = scrapy.Field()
    positive_emotion = scrapy.Field()
    negative_emotion = scrapy.Field()
    total_score = scrapy.Field()
    film_result = scrapy.Field()
