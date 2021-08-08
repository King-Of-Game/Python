#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/21/2021 3:15 PM
# __software__ : PyCharm

import re

# 方法一：
ex = r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

# img_list = re.findall(ex, page_text, re.S)
# print(img_list)

# 方法二：
p1 = re.compile(r'//.*?pictures.*?.(?:jpg|png|gif)')

# img_list = p1.findall(page_text)
# # print(img_list)