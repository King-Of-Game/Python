#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/21/2021 1:40 PM
# __software__ : PyCharm


'''

给定一个字符串，然后判断指定的子字符串是否存在于该字符串中。

'''


# 方法一
def findSubInString(string, sub_str):
    # 返回 -1: 不存在; 其它数字表示第一次出现的位置
    print(string.find(sub_str))
    if string.find(sub_str) == -1:
        print(f'{string} 中不存在 {sub_str}')
    else:
        print(f'{string} 中存在 {sub_str}')


# 方法二
def findSubInString1(string, sub_str):
    # 返回0: 存在, -1: 不存在
    if sub_str in string:
        print(f'{string} 中存在 {sub_str}')
    else:
        print(f'{string} 中不存在 {sub_str}')


if __name__ == '__main__':
    string = input('请输入一个字符串: ')
    sub_str = input('请输入一个子字符串: ')

    findSubInString(string, sub_str)
    # findSubInString1(string, sub_str)
