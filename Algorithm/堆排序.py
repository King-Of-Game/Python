#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/3/2021 7:55 PM
# __software__ : PyCharm

'''

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
堆排序可以说是一种利用堆的概念来排序的选择排序。

'''


def heapify(arr, length, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < length and arr[i] < arr[l]:
        largest = l

    if r < length and arr[i] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        # 此时largest位置的数字（也就是最开始输入那个lis[i]）处于待定状态，需要在它所有根部中确定其位置
        heapify(arr, length, largest)


def heapSort(arr):
    length = len(arr)

    # Build a maxheap.
    for i in range(length, -1, -1):
        # 先把堆调整好小根堆的状态，在全堆中逐个调整每个数字的位置，调整的方法是在它所有根部中确定其位置
        heapify(arr, length, i)

    # 一个个交换元素
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        # 把新上来的0号安排到合适的位置上去,其中i指的是要调整的堆的范围
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print(f"排列前: {arr}")

    heapSort(arr)
    print(f"从小到大堆排序后: {arr}")
