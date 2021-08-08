#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/20/2021 1:28 PM
# __software__ : PyCharm


'''

列表切片的时候两个索引值相同的话： 结果为空
range()函数也如此

list[1:1] = ''
for i in range(2,2):
    i = ''

'''


# 清空列表
def clearList():
    RUNOOB = [6, 0, 4, 1]
    print('清空前:', RUNOOB)

    RUNOOB.clear()
    print('清空后:', RUNOOB)


# 使用 list 对象的 copy() 方法复制列表
def copyList():
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = li1.copy()
    print("原始列表:", li1)
    print("复制后列表:", li2)

    print(f'{id(li1)} \n{id(li2)}')


# 元素切片
def copyList1():
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = li1[:]
    print("原始列表:", li1)
    print("复制后列表:", li2)

    print(f'{id(li1)} \n{id(li2)}')


# 使用 extend() 方法
def copyList2():
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = []
    li2.extend(li1)
    print("原始列表:", li1)
    print("复制后列表:", li2)

    print(f'{id(li1)} \n{id(li2)}')


# 使用 list() 方法
def copyList3():
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = list(li1)
    print("原始列表:", li1)
    print("复制后列表:", li2)

    print(f'{id(li1)} \n{id(li2)}')


# 计算元素在列表中出现的次数
def countElement():
    lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    count = lst.count(8)
    print(f'8 出现了: {count} 次')


def countElement1():
    lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    count = 0
    for i in lst:
        if 8 == i:
            count += 1
    print(f'8 出现了: {count} 次')


# 列表元素求和
def sumList():
    arr = [12, 3, 4, 15]
    result = sum(arr)
    print(f'{arr}\n的元素之和为: {result}')


def sumList1():
    arr = [12, 3, 4, 15]
    result = 0
    for i in arr:
        result += i
    print(f'{arr} 的元素之和为: {result}')


# 列表元素之积
def productList():
    list1 = [1,2,3,4,5]
    result = 1
    for i in list1:
        result *= i
    print(f'{list1} 中元素的乘积: {result}')


# 递归求元素之积
def productList1(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return list1.pop(0) * productList1(list1)


# 查找列表中最小元素
def minList():
    list1 = [10, 20, 4]
    print(f'{list1} 中最小元素是: ', end='')
    list1.sort()
    result = list1[0]
    print(f'{result}')


def minList1():
    list1 = [10, 20, 4]
    result = min(list1)
    print(f'{list1} 中最小元素是: {result}')


def minList2():
    list1 = [10, 20, 4]
    result = list1[0]
    for i in list1:
        if i < result:
            result = i
    print(f'{list1} 中最小元素是: {result}')


# 查找列表中最大元素
def maxList():
    list1 = [10, 20, 4]
    print(f'{list1} 中最大元素是: ', end='')
    list1.sort()
    result = list1[-1]
    print(f'{result}')


def maxList1():
    list1 = [10, 20, 4]
    result = max(list1)
    print(f'{list1} 中最大元素是: {result}')


def maxList2():
    list1 = [10, 20, 4]
    result = list1[0]
    for i in list1:
        if i > result:
            result = i
    print(f'{list1} 中最大元素是: {result}')




if __name__ == '__main__':
    # clearList()

    # copyList()
    # copyList1()
    # copyList2()
    # copyList3()

    # countElement()
    # countElement1()

    # sumList()
    # sumList1()

    # productList()
    # list1 = [1, 2, 3, 4, 5]
    # print(f'{list1} 中元素的乘积: {productList1(list1)}')

    # minList()
    # minList1()
    # minList2()

    # maxList()
    # maxList1()
    maxList2()


