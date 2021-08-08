#! /usr/bin/env python³
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/20/2021 2:55 PM
# __software__ : PyCharm

'''

计算公式 1³ + 2³ + 3³ + 4³ + …+ n³

实现要求：
输入 : n = 5
输出 : 225
公式 : 1³ + 2³ + ³³ + 4³ + 5³ = 225


输入 : n = 7
输入 : 784
公式 : 1³ + 2³ + ³³ + 4³ + 5³ + 6³ + 7³ = 784

'''


def nCubeSum():
    n = int(input('请输入一个正整数: '))
    result = 0
    for i in range(1, n+1):
        result += i**3
    print(f'1³ + 2³ + 3³ + … + {n}³ = {result}')


if __name__ == '__main__':
    nCubeSum()