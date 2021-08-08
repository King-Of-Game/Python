#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/16/2021 1:02 PM
# __software__ : PyCharm

'''

九九乘法表

'''


# 每一行都从 1 开始
def multiplication_tab1():
    for i in range(1, 10):
        for j in range(1, i+1):
            result = f'{j}x{i}={j * i}'.ljust(8)
            print(result, end='')
        print('\n' + '-' * len(result) * i)


# 一行代码打印99乘法表(x: 行, y: 列)
def multiplication_tab2():
    print('\n'.join(['\t'.join([f'{y}x{x}={x*y}'for y in range(1, x)]) for x in range(1, 10)]))


if __name__ == '__main__':
    multiplication_tab1()
    # multiplication_tab2()
