#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/19/2021 11:25 AM
# __software__ : PyCharm


'''

使用内置函数实现：字符串大小写转换

'''


def upper_lower():
    string = "www.runoob.com"
    print(string.upper())  # 把所有字符中的小写字母转换成大写字母
    print(string.lower())  # 把所有字符中的大写字母转换成小写字母
    print(string.capitalize())  # 把第一个字母转化为大写字母，其余小写
    print(string.title())  # 把每个单词的第一个字母转化为大写，其余小写


if __name__ == '__main__':
    upper_lower()
