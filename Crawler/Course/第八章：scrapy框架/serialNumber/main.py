#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 12/5/2020 2:19 PM
# __software__ : PyCharm

from scrapy.cmdline import execute
import os
import sys

#添加当前项目的绝对地址
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#执行 scrapy 内置的函数方法execute，  使用 crawl 爬取并调试，最后一个参数fhk 是我的爬虫文件名
execute(['scrapy', 'crawl', 'fhk'])

