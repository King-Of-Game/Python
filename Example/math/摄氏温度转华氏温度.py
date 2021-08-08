#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 3:14 PM
# __software__ : PyCharm

'''
摄氏温度 与 华氏温度公式 关系式：
celsius * 1.8 = fahrenheit - 32
'''


def get_fahrenheit():
    celsius = float(input('请输入摄氏温度 (°C) ：'))
    fahrenheit = celsius * 1.8 + 32
    print(f'华氏温度为: {fahrenheit} °F'.format(fahrenheit))


if __name__ == '__main__':
    get_fahrenheit()