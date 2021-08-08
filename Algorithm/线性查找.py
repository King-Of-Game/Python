#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/23/2021 7:42 PM
# __software__ : PyCharm


'''

线性查找指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。
（从第一个到最后一个依次查找）

'''

import random


def lineSearch(lst, num):
    for i in lst:
        if i == num:
            print(f'您所查找的数字是 {lst} 的第 {lst.index(i)+1} 个元素')
            return True
    else:
        print(f'很遗憾，随机生成的列表中没有符合条件的元素:\n{lst}')


if __name__ == '__main__':
    while True:
        input_txt = input('输入q退出: ')
        if input_txt in ['q', 'Q']:
            break

        target_list = random.sample(range(10), 10)  # 生成 0~9 这10个数字并打乱顺序的列表
        num = int(input('请输入你想查找的数字: '))
        lineSearch(target_list, num)



