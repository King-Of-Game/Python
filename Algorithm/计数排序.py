#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/6/2021 12:56 PM
# __software__ : PyCharm

'''
计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。

作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

ord(字符): 返回 ASCII字符 对应的十进制
chr(十进制): 返回十进制对应的 ASCII码
'''


def countSort(arr):
    count = [0 for i in range(256)]  # 0~255 的索引范围对应ascii 字符，值对应这个字符的数量
    new_arr = []

    for i in arr:
        # print(f"{i}: {ord(i)}")
        count[ord(i)] += 1

    for i in range(len(count)):
        if count[i] != 0:
            print(f"{chr(i)} 的 ascii 码为: {i}, 数量为: {count[i]}")

            for num in range(count[i]):
                new_arr.append(chr(i))

    print(f"按照 ascii码 计数排序后: {''.join(new_arr)}")


if __name__ == '__main__':
    arr = "wwwrunoobcom"
    countSort(arr)

