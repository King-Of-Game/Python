#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/3/2021 2:56 PM
# __software__ : PyCharm

'''

归并排序（英语：Merge sort，或 mergesort），是创建在归并操作上的一种有效的排序算法。
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

分治法:
分割：递归地把当前序列平均分割成两半。
集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。

'''


# 从小到大
def mergeSort1(lst):
    # 当数组的长度为1时，此时数组就时有序数组
    if len(lst) <= 1:
        return lst

    mid_index = len(lst) // 2
    left = mergeSort1(lst[:mid_index])
    right = mergeSort1(lst[mid_index:])

    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    merged.extend(left if left else right)  # 左边和右边列表经过上一步之后，如果某个列表有剩余元素，就把该列表合并到新列表中
    # print(merged)
    return merged


# 从大到小
def mergeSort2(lst):
    if len(lst) <= 1:
        return lst

    mid_index = len(lst) // 2
    left = mergeSort2(lst[:mid_index])
    right = mergeSort2(lst[mid_index:])

    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] >= right[0] else right.pop(0))
    merged.extend(left if left else right)
    # print(merged)
    return merged


if __name__ == '__main__':
    lst = [6, 202, 100, 301, 38, 8, 1]
    print(f"排序前: {lst}")

    new_lst = mergeSort1(lst)
    print(f"从小到大归并排序后: {new_lst}")
    new_lst = mergeSort2(lst)
    print(f"从大到小归并排序后: {new_lst}")






