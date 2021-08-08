#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/4/25 16:51
# __software__ : PyCharm

import functools
from decorator import decorator


def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@decorator1
def wrapped1():
    print(f'{wrapped1.__name__}')


if __name__ == '__main__':
    result = wrapped1()
    print(result)