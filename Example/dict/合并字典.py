#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/22/2021 1:39 PM
# __software__ : PyCharm

'''

将两个字典合并为一个

'''


# 使用 update() 方法，把另一个字典合并到调用该方法的字典中
def updateDict(dict1, dict2):
    dict2.update(dict1)  # dict2 合并了 dict1
    print(f'合并后的dict2: {dict2}')


#  使用 **，函数将参数以字典的形式导入
def mergeDict(dict1, dict2):
    new_dict = {**dict1, **dict2}
    print(f'合并后的new_dict: {new_dict}')


if __name__ == '__main__':
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    print(f'原始两个字典:\ndict1: {dict1}\ndict2: {dict2}')

    updateDict(dict1, dict2)
    mergeDict(dict1, dict2)