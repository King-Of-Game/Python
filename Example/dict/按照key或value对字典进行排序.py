#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/21/2021 5:06 PM
# __software__ : PyCharm

'''

给定一个字典，然后按键(key)或值(value)对字典进行排序。

'''


# 按键(key)排序
def sortByKey():
    dict1 = {
        2: 56,
        1: 2,
        5: 12,
        4: 24,
        6: 18,
        3: 323
    }

    print(f"排序前: {dict1}")

    list1 = sorted(dict1.items())
    dict1 = dict(list1)  # dict() 函数只能从元组列表中构建字典：[(1, 2), (2, 56), (3, 323), (4, 24), (5, 12), (6, 18)]
    print(f'按键(key)排序后: {dict1}')


# 按值(value)排序
def sortByValue():
    dict1 = {
        2: 56,
        1: 2,
        5: 12,
        4: 24,
        6: 18,
        3: 323
    }

    print(f"排序前: {dict1}")

    # dict1.items() 返回一个元组列表: [(1, 2), (2, 56), (3, 323), (4, 24), (5, 12), (6, 18)]
    list1 = sorted(dict1.items(), key=lambda item: (item[1], item[0]))  # item 是每个被迭代的元组对象, key是待排序的数据
    dict1 = dict(list1)
    print(f'按键(value)排序后: {dict1}')


# 字典列表排序
def sortToDictLIst():
    lis = [
        {"name": "Taobao", "age": 100},
        {"name": "Runoob", "age": 7},
        {"name": "Google", "age": 100},
        {"name": "Wiki", "age": 200}
    ]
    print('排序前:')
    for i in lis: print(i)

    # 根据 age 升序排序
    print('根据 age 升序排序后:')
    lis1 = sorted(lis, key=lambda item: item['age'])
    for i in lis1: print(i)

    # 根据 age 降序排序
    print('根据 age 降序排序后:')
    lis2 = sorted(lis, key=lambda item: item['age'], reverse=-1)
    for i in lis2: print(i)

    # 先按 age 排序, 再按 name 排序
    print('先按 age 排序, 再按 name 排序:')
    lis3 = sorted(lis, key=lambda item: (item['age'], item['name']))
    print('\n'.join(str(i) for i in lis3))




if __name__ == '__main__':
    # sortByKey()
    # sortByValue()
    sortToDictLIst()