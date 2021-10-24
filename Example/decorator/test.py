#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/4/25 16:51
# __software__ : PyCharm

from decorator import decorator
import time


@decorator
def wrapper(func, *args, **kwargs):
    print('start timing')
    start_time = time.time()
    func(*args, **kwargs)
    print(f"总耗时：{time.time() - start_time}")


@wrapper
def func(*args, **kwargs):
    print(f"func的签名：{func.__name__}")
    for i in range(kwargs['num']):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    func(num=3)