#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 12:53 PM
# __software__ : PyCharm

import cmath    # 导入复数数学模块


# 只适用于正数
def square_root(number):
    result = number ** 0.5
    print(result)


# 适用于负数和复数
def square_root2(num):
    result = cmath.sqrt(num)
    print(f'{num} 的平方根为{result.real:.3f}+{result.imag:.3f}j'.format(num, result))


if __name__ == '__main__':
    square_root(9)
    square_root2(-8)