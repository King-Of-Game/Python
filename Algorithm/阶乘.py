#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/27/2021 9:26 PM
# __software__ : PyCharm
'''
阶乘
5 的阶乘：1*2*3*4*5
'''


# 递归求阶乘
def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)


# 普通求阶乘
def factorial1(n):
    result1 = 1
    while n > 1:
        result1 *= n
        n -= 1
    print(f'{number} 的阶乘是: {result1}')


if __name__ == '__main__':
    number = 5

    result = factorial(number)
    print(f'{number} 的阶乘是: {result}')

    factorial1(number)