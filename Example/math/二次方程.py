#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 1:01 PM
# __software__ : PyCharm

'''
二次方程：ax²+bx+c = 0
a、b、c 为用户提供的实数，a ≠ 0
'''

# 导入 cmath(复杂数学运算) 模块
import cmath


def quadratic_equation():
    print('*** ax²+bx+c=0 ***')
    a = int(input('请输入a：'))
    b = int(input('请输入b：'))
    c = int(input('请输入c：'))

    deta = (b**2) - (4*a*c)

    x1 = (-b + cmath.sqrt(deta)) / (2*a)
    x2 = (-b - cmath.sqrt(deta)) / (2*a)

    print(f'x1: {x1}, x2: {x2}'.format(x1, x2))


if __name__ == '__main__':
    quadratic_equation()