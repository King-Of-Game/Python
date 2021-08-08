#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/23/2021 8:23 PM
# __software__ : PyCharm


'''

插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

'''


# 从小到大排列
def insertionSort(lst):
    for i in range(1, len(lst)):

        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

    print(f'从小到大插入排序后: {lst}')


# 从大到小
def insertionSort1(lst):
    # 从第二个元素开始遍历，此时第一个元素自然就是有序序列
    for i in range(1, len(lst)):

        key = lst[i]
        j = i - 1
        while j >= 0 and key > lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

    print(f'从大到小插入排序后: {lst}')


if __name__ == '__main__':
    lst = [0, 6, 1, 7, 8, 3, 9, 4, 5, 2]
    print(f'原始列表: {lst}')

    # insertionSort(lst)
    insertionSort1(lst)












