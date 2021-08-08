#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 2:45 PM
# __software__ : PyCharm

'''
根据三角形三条边的长度计算面积
'''
def triangle_area():

    x = float(input('输入三角形第一边长（单位:cm）'))
    y = float(input('输入三角形第二边长（单位:cm）'))
    z = float(input('输入三角形第三边长（单位:cm）'))

    # 计算半周长
    c = (x + y + z) / 2

    # 计算面积
    area = (c * (c - x) * (c - y) * (c - z)) ** 0.5

    print(f'三角形的面积为: {area:.2f} (cm²)'.format(area))



if __name__ == '__main__':
    triangle_area()