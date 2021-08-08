#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 3/1/2021 9:02 PM
# __software__ : PyCharm


def removeSpace(string):
    print(f'移除首尾空格前: {string}, 字符串长度: {len(string)}')
    if string[:1] == ' ':
        string = string[1:]
    if string[-1:] == ' ':
        string = string[:-1]
    print(f'移除首尾空格后: {string}, 字符串长度: {len(string)}')


if __name__ == '__main__':
    while True:
        string = input('请输入一串字符(输入 q/Q 退出)\n')
        if string in 'qQ':
            break
        removeSpace(string)
