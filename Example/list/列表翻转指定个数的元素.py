#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/20/2021 4:08 PM
# __software__ : PyCharm

'''

定义一个整型数组，并将指定个数的元素翻转到数组的尾部。

例如:
(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
原始数组：[1,2,3,4,5,6,7]
翻转后：[3,4,5,6,7,1,2]

'''


# 利用列表的 pop() 方法能返回元素的特性
def reverseList():
    arr = [1,2,3,4,5,6,7]
    print(f'原始数组: {arr}')

    count = int(input('请输入将前面几个元素翻转到后面: '))

    if count > len(arr):
        print('翻转的元素个数超出数组长度!')
        reverseList()
    else:
        while count > 0:
            arr.append(arr.pop(0))
            count -= 1
        print(f'翻转后: {arr}')


# 利用列表切片
def reverseList1():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(f'原始数组: {arr}')

    count = int(input('请输入将前面几个元素翻转到后面: '))

    if count > len(arr):
        print('翻转的元素个数超出数组长度!')
        reverseList1()
    else:
        arr = arr[count:] + arr[:count]
        print(f'翻转后: {arr}')


if __name__ == '__main__':
    reverseList()
    reverseList1()
