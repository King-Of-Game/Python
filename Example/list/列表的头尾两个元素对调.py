#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/20/2021 4:22 PM
# __software__ : PyCharm

'''

定义一个列表，并将列表中的头尾两个元素对调。

例如：
对调前 : [1, 2, 3]
对调后 : [3, 2, 1]

'''

def swapList()\
        :
    list1 = [1, 2, 3, 4]
    print(f'原始列表: {list1}')

    list1[0], list1[-1] = list1[-1], list1[0]
    print(f'头尾对调后: {list1}')


def swapList1():
    list1 = [1, 2, 3, 4]
    print(f'原始列表: {list1}')

    temp = list1[0]
    list1[0] = list1[-1]
    list1[-1] = temp
    print(f'头尾对调后: {list1}')


def swapList2():
    list1 = [1, 2, 3, 4]
    print(f'原始列表: {list1}')

    get = list1[-1], list1[0]

    list1[0], list1[-1] = get
    print(f'头尾对调后: {list1}')


if __name__ == '__main__':
    # swapList()
    # swapList1()
    swapList2()
