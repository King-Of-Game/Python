#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/28/2021 5:57 PM
# __software__ : PyCharm


def delRepeatElement(lst):
    lst = list(set(lst))
    print(f'清除重复元素后测列表为: {lst}')


def delRepeatElement1(lst):
    dict1 = {}
    for i in lst:
        dict1[i] = 1
    lst = [i for i in dict1.keys()]
    print(f'清除重复元素后测列表为: {lst}')


if __name__ == '__main__':
    lst = [1,1,2,2,3,3]

    # delRepeatElement(lst)
    delRepeatElement1(lst)
