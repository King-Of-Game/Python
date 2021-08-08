#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 12/31/2020 2:50 PM
# __software__ : PyCharm


'''

翻转列表
方法一：使用内置函数 reversed()
方法二：使用列表的内置方法 list.sort()
方法二：使用列表的第三个参数

'''


def reversed_list1():
    list1 = [1,2,3]
    new_list = [i for i in reversed(list1)]
    print(new_list)


def reversed_list2():
    list1 = [1,2,3]
    list1.sort(reverse=True)
    # list1.reverse()
    print(list1)


def reversed_list3():
    list1 = [1,2,3]
    new_list = list1[::-1]
    print(new_list)


if __name__ == '__main__':
    reversed_list1()
    reversed_list2()
    reversed_list3()



