# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NeteasyproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    module = scrapy.Field()
    title = scrapy.Field()
    new_detail = scrapy.Field()

