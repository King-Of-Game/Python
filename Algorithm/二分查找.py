#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/23/2021 1:06 PM
# __software__ : PyCharm

'''

二分搜索是一种在有序数组中查找某一特定元素的搜索算法。
搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；
如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
如果在某一步骤数组为空，则代表找不到。
这种搜索算法每一次比较都使搜索范围缩小一半。

'''

'''
arr: 从该列表中检索元素
left: 检索区间最左边的索引
right: 检索区间最右边的索引
search_item: 被检索的元素
'''
# 递归版本
def binarySearch(arr, left, right, search_item):
    if right >= left:

        min_index = (left+right) // 2
        if arr[min_index] == search_item:
            print(f'{search_item} 是 {arr} 中的第 {min_index + 1} 个元素')

        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif search_item < arr[min_index]:
            binarySearch(arr, left, min_index-1, search_item)

        # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            binarySearch(arr, min_index+1, right, search_item)  # len=2, min=3

    else:
        print(f'在 {arr} 中找不到 {search_item} !')


# 非递归版本
def binarySearch1(arr, left, right, search_item):
    while left <= right:
        mid = (left+right) // 2
        if search_item == arr[mid]:
            print(f'{search_item} 是 {arr} 中的第 {mid + 1} 个元素')
            break
        elif search_item < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        print(f'在 {arr} 中找不到 {search_item} !')


if __name__ == '__main__':
    arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    length = len(arr)
    search_item = 2  # 被查找的元素

    binarySearch(arr, 0, length-1, search_item)
    # binarySearch1(arr, 0, length - 1, search_item)

