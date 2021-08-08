#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 10:09 PM
# __software__ : PyCharm

'''

整数的阶乘（英语：factorial）
是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。

'''


# 递归求阶乘
def factorial1(number):
    if number <= 1:
        return 1

    else:
        return number * factorial1(number - 1)


# 普通求阶乘
def factorial2():
    result = 1
    try:
        number = int(input('请输入一个正整数：'))
    except ValueError:
        print('请输入正整数！')
        return factorial2()

    if number < 0:
        print('负数没有阶乘！')
        return factorial2()
    elif number == 0:
        print('0 的阶乘是 1')
    else:
        for i in range(1, number+1):
            result = result * i
        print(f'{number}的阶乘是{result}')


if __name__ == '__main__':
    # num = 5
    # result1 = factorial1(num)
    # print(f'{num} 的阶乘是:{result1}')

    factorial2()