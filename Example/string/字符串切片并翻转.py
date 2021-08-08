#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/21/2021 4:27 PM
# __software__ : PyCharm


'''

给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。

'''


# 头部切片翻转
def reversedHead(string, length):
    part1 = string[:length]
    part2 = string[length:]
    string = part2 + part1
    print(f'头部前: {length} 个翻转后: {string}')


# 尾部切片翻转
def reversedTail(string, length):
    part1 = string[:-length]
    part2 = string[-length:]
    string = part2 + part1
    print(f'尾部前: {length} 个翻转后: {string}')


if __name__ == '__main__':
    string = 'Runoob'
    length = 2
    print(f'翻转前: {string}')

    reversedHead(string, length)
    reversedTail(string, length)

