#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/22/2021 11:18 AM
# __software__ : PyCharm

'''

给定一个字典， 移除字典点键值(key/value)对。

'''


# 使用 del 移除
def delDict(dict1):
    try:
        del dict1['Zhihu']
        print(f'字典移除后: {dict1}')
    except KeyError:
        print('没有这个 key ')


# 使用 pop() 移除
def popDict(dict1):
    try:
        dict1.pop('Zhihu')  # pop 函数会返回该 key 的 value
        print(f'字典移除后: {dict1}')
    except KeyError:
        print('没有这个 key ')


# 使用 items() 移除
def itemsDict(dict1):
    new_dict = {key: value for key, value in dict1.items() if key != 'Zhihu'}

    print(f'字典移除后: {new_dict}')



if __name__ == '__main__':
    test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
    print(f'字典移除前: {test_dict}')

    # delDict(test_dict)
    # popDict(test_dict)
    itemsDict(test_dict)