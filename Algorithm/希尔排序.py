#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/6/2021 2:25 PM
# __software__ : PyCharm

'''

希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

希尔排序的基本思想是：
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
arr = [12, 34, 54, 2, 3]
'''


# 从小到大
def shellSort(arr):
    length = len(arr)
    gap = length // 2

    while gap > 0:

        for i in range(gap, length):

            temp = arr[i]
            j = i
            while j >= gap and temp < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print(arr)

        gap = gap // 2

    print(f"从小到大希尔排序后: {arr}")


# 从大到小
def shellSort1(arr):
    length = len(arr)
    gap = length // 2

    while gap > 0:

        for i in range(gap, length):

            temp = arr[i]
            j = i
            while j >= gap and temp > arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp

        gap = gap // 2

    print(f"从大到小希尔排序后: {arr}")


if __name__ == '__main__':
    arr = [12, 34, 54, 2, 3]
    print(f"希尔排序前: {arr}")

    shellSort(arr)
    # shellSort1(arr)