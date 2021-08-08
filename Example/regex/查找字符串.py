#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 3/1/2021 11:19 AM
# __software__ : PyCharm

'''
match(): 只有在 0 位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
search(): 会扫描整个 字符串 查找匹配，只返回第一个匹配的结果
'''

import re


# 使用findall() 提取url
def findall(string):
    result = re.findall(r'https?://\w+\.\w+.[com|\w]+', string)
    print(f'findall 匹配了 {len(result)} 个url: {", ".join(result)}')


# 使用 match() 只能从 字符串 开始位置开始匹配字符
def match(string):
    result = re.match(r'unoob', string)
    print(f'match 匹配 "unoob": {result}')

    result = re.match(r'Runoob', string)
    print(f'match 匹配 "Runoob": {result}')


# 使用 search() 扫描整个 字符串 查找匹配
def search(string):
    result = re.search(r'unoob', string)
    print(f'search 匹配 "unoob: {result}"')

    result = re.search(r'http', string)
    print(f'search 匹配 "http": {result}')

    result = re.search(r'https', string)
    print(f'search 匹配 "https": {result}')


if __name__ == '__main__':
    string = 'Runoob 的网页地址为：https://www.runoob.com , 特殊网址1：http://tool.oschina.net/regex'

    findall(string)
    match(string)
    search(string)