#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/21/2021 4:02 PM
# __software__ : PyCharm

'''

给定一个字符串，然后将其翻转，逆序输出。

'''


# 使用字符串切片
def reversedString(string):
    string = string[::-1]
    print(f'翻转后: {string}')


# 使用内置函数: reversed()
def reversedString1(string):
    string = ''.join(reversed(string))
    print(f'翻转后: {string}')


if __name__ == '__main__':
    string = 'Runoob'
    print(f'翻转前: {string}')

    reversedString(string)
    reversedString1(string)
