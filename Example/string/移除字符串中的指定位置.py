#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/21/2021 1:13 PM
# __software__ : PyCharm

'''
移除字符串中指定位置的字符
'''


# 方法一
def removeChar(string, index):
    result = ''
    for i in range(len(string)):
        if i == index - 1:
            continue
        result += string[i]
    print(f'移除后: {result}')


# 方法二
def removeChar1(string, index):
    result = string[:index-1] + string[index:]
    print(f'移除后: {result}')


# 方法三
def removeChar2(string, index):
    result = string.replace(string[index-1], '', 1)
    print(f'移除后: {result}')





if __name__ == '__main__':
    string = input('请输入一串字符: ')
    index = int(input('您希望移除第几个字符? '))

    if index > len(string):
        print('超出字符串长度！')
    print(f'移除前: {string}')

    # removeChar(string, index)
    # removeChar1(string, index)
    removeChar2(string, index)


