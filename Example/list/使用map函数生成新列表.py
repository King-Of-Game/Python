#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/28/2021 6:42 PM
# __software__ : PyCharm

'''
map() 会根据提供的函数对指定序列做映射。

map(function, iterable, ...)
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

Python 2.x 返回列表。
Python 3.x 返回迭代器。

'''


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def mapExample1(name):
    return name.capitalize()


# 计算平方
def mapSquare(num):
    return num ** 2


if __name__ == '__main__':
    lst = ['adam', 'LISA', 'barT']

    new_lst = list(map(mapExample1, lst))  # 因为map() 在py3中返回迭代器，所以要用 list()转化
    print(f'原始列表: {lst}, 格式化后: {new_lst}')

    lst = [i for i in range(1, 5)]
    new_lst = list(map(mapSquare, lst))
    print(f'原始列表: {lst}, 逐个平方后: {new_lst}')
