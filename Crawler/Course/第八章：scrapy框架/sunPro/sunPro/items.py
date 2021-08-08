# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    novel_category = scrapy.Field()
    novel_name = scrapy.Field()
    novel_author = scrapy.Field()
    # novel_popularity = scrapy.Field()
    # novel_synopsis = scrapy.Field()


class DetailItem(scrapy.Item):
    novel_popularity = scrapy.Field()
    novel_synopsis = scrapy.Field()
