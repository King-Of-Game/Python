#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 2:57 PM
# __software__ : PyCharm

'''
圆的面积公式为：S = ∏r²
公式中 r 为圆的半径（单位:cm）
'''


def circle_area(r):
    PI = 3.142
    S = PI * r**2
    print(f'半径为{r}的圆的面积是：{S:.2f} cm²'.format(r, S))


if __name__ == '__main__':
    circle_area(5)