#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/22/2021 10:14 AM
# __software__ : PyCharm


'''

计算字典之和
方法一：循环遍历
方法二：使用 functools 包的 reduce 模块

'''

from functools import reduce


# 方法一
def sumDict(dict1):
    sum_dict = 0
    for i in dict1.values():
        sum_dict += i
    print(f'该字典的和为: {sum_dict}')


# 方法二
def sumDict1(dict1):
    sum_dict = reduce(lambda x, y: x+y, dict1.values())
    print(sum_dict)


if __name__ == '__main__':
    dict1 = {'a': 100, 'b': 200, 'c': 300}
    print(f'待求和的字典: {dict1}')

    # sumDict(dict1)
    sumDict1(dict1)
