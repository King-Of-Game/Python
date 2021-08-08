# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    serial_number = scrapy.Field()
    video_name = scrapy.Field()
    author_name = scrapy.Field()
    video_tag = scrapy.Field()
    publish_date = scrapy.Field()

    video_ticket = scrapy.Field()

