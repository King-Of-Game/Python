#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 8:44 PM
# __software__ : PyCharm

'''
质数要满足两个条件
1. 大于 1 的自然数
2. 只能被 1 和它本身整除
'''


# number 是否为质数
def is_primeNumber(number):
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} 不是质数：{number} = {i} * {number//i}')
            break
    else:
        print(f'{number} 是质数')


# number 以内的质数
def is_primeNumber1(number):
    for x in range(2, (number + 1)):
        for i in range(2, x):
            if x % i == 0:
                print(f'{x} 不是质数：{x} = {i} * {x // i}')
                break
        else:
            print(f'{x} 是质数')


if __name__ == '__main__':
    is_primeNumber1(10)

