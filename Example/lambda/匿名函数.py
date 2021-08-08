#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/28/2021 11:00 AM
# __software__ : PyCharm


# 匿名函数求和
def add():
    return lambda x, y: x+y


# 匿名函数求积
def multiply(multiple):
    return lambda num: num * multiple


if __name__ == '__main__':
    add1 = add()
    result = add1(1, 2)
    print(result)

    # 求积
    multiple = 2
    multiply1 = multiply(multiple)
    print(f'倍数为 {multiple}: {multiple} * 3 = {multiply1(3)}')

    multiple = 3
    multiply2 = multiply(multiple)
    print(f'倍数为 {multiple}: {multiple} * 3 = {multiply2(3)}')

    multiple = 2
    multiply1 = multiply(multiple)
    list1 = [multiply1(i) for i in range(1, 10)]
    print(f'倍数为 {multiple}: {list1}')


