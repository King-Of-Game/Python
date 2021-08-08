#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/16/2021 9:20 PM
# __software__ : PyCharm

'''

输入两个数字，计算他们之间的最大公约数

'''


def hcf():
    num1 = int(input('请输入第一个数字: '))
    num2 = int(input('请输入第二个数字: '))

    if num1 > num2:
        smaller = num2
    else:
        smaller = num1

    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            print(f'{num1} 和 {num2} 之间的最大公约数是: {i}')
            break


# 辗转相除法(不用判断大小)
def f1(a, b):
    while b != 0:
        a, b = b, a % b
    print(a)


# 相减法
def f2(a, b):
    while a != b:
        a, b = min(a, b), abs(a-b)
    print(a)


if __name__ == '__main__':
    hcf()

