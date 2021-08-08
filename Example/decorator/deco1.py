#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/28/2021 5:32 PM
# __software__ : PyCharm

'''
装饰器是要把原来的函数装饰成新的函数，并且返回这个函数本身的高阶函数
'''
import time
import functools

from decorator import decorator


# normal decorator example1
def decorator1(func):
    def wrapper1(*args, **kwargs):
        print('准备执行...')
        func(*args, **kwargs)
        print('执行成功！')
    return wrapper1


@decorator1
def wrapped1():
    print(f'被装饰函数1: {wrapped1.__name__}')
    print('签名指向 => wrapper1')


# normal decorator example2
def decorator2(func):
    @functools.wraps(func)
    def wrapper2(*args, **kwargs):
        print('start executing...')
        func(*args, **kwargs)
        print('execution succeed')
    return wrapper2


@decorator2
def wrapped2():
    print(f'被装饰函数2: {wrapped2.__name__}')
    print('签名指向 => wrapped2')


# use decorator module example1
@decorator
def wrapper3(func, *args, **kwargs):
    print('starting executing...')
    func(*args, **kwargs)
    print('execution succeed')


@wrapper3
def wrapped3():
    print(f'被装饰函数3: {wrapped3.__name__}')
    print(f'签名指向 => wrapped3')


# use decorator module example2
@decorator
def wrapper4(func, timelimit=60, *args, **kwargs):
    print(f'starting executing...')
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    dt = end_time - start_time
    if dt > timelimit:
        print(f'超时完成: {dt} s')
    else:
        print(f'限时内完成: {dt} s')
    print('execution succeed!')
    return result


@wrapper4(timelimit=60)
def wrapped4(*args, **kwargs):
    print(f'被装饰函数4: {wrapped4.__name__}')
    print('签名指向 => wrapped4')
    print(args)
    print(kwargs)


if __name__ == '__main__':
    wrapped1()
    # wrapped2()
    # wrapped3()
    # wrapped4(1, 2, 3, a=1, b=2, c=3)