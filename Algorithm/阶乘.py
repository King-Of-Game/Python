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
    while n:
        result1 *= n
        n -= 1
    return result



if __name__ == '__main__':
    number = 5

    result = factorial(number)
    print(f'{number} 的阶乘是: {result}')

    result = factorial1(number)
    print(f'{number} 的阶乘是: {result}')