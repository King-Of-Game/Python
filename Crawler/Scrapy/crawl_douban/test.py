#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 12/14/2020 12:17 PM
# __software__ : PyCharm


list1 = ['好','hot', '而且']
single_word_index_list = []
new_words_list = []

for item in list1:

    if len(item) == 1:
        continue
    new_words_list.append(item)


print(new_words_list)