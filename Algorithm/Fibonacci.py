#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/7/2021 3:14 PM
# __software__ : PyCharm


# 递归求第...个斐波那契数
def digui_feibo(count):
    if count <= 1:
        return count
    else:
        return digui_feibo(count-1) + digui_feibo(count - 2)


# 结合上面的递归方法求前...个斐波那契数
def feibo():
    for i in range(6):
        print(f'第{i+1}个斐波那契数为: {digui_feibo(i)}')


# 输出前...个斐波那契数
def putong_feibo(num):
    a, b = 0, 1
    count = 0
    while count < num:
        print(f'第 {count+1} 个斐波那契数为: {a}')
        a, b = b, a + b
        count += 1


if __name__ == '__main__':
    feibo()
    putong_feibo(6)











