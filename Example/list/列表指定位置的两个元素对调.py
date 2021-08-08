#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/20/2021 4:28 PM
# __software__ : PyCharm

'''

定义一个列表，并将列表中的指定位置的两个元素对调。

例如，对调第一个和第三个元素：
对调前 : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
对调后 : [19, 65, 23, 90]

'''


def swapList():
    list1 = [1, 2, 3, 4]
    print(f'原始列表: {list1} \n请输入两个对调元素的位置: ')

    pos1 = int(input('位置1: '))
    pos2 = int(input('位置2: '))

    if pos1 > len(list1) or pos2 > len(list1):
        print('位置超出列表长度！')
        return swapList()
    else:
        list1[pos1 - 1], list1[pos2 - 1] = list1[pos2 - 1], list1[pos1 - 1]
        print(f'将第 {pos1} 与第 {pos2} 个元素对调后: {list1}')


def swapList1():
    list1 = [1, 2, 3, 4]
    print(f'原始列表: {list1} \n请输入两个对调元素的位置: ')

    pos1 = int(input('位置1: '))
    pos2 = int(input('位置2: '))

    temp = list1[pos1 - 1]
    list1[pos1 - 1] = list1[pos2 - 1]
    list1[pos2 - 1] = temp

    print(f'将第 {pos1} 与第 {pos2} 个元素对调后: {list1}')


def swapList2():
    list1 = [1, 2, 3, 4]
    print(f'原始列表: {list1} \n请输入两个对调元素的位置: ')

    pos1 = int(input('位置1: '))
    pos2 = int(input('位置2: '))

    get = list1[pos2 - 1], list1[pos1 - 1]
    list1[pos1 - 1], list1[pos2 - 1] = get

    print(f'将第 {pos1} 与第 {pos2} 个元素对调后: {list1}')


if __name__ == '__main__':
    # swapList()
    # swapList1()
    swapList2()
