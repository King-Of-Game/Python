#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 4:52 PM
# __software__ : PyCharm

'''

判断字符串是否为数字：

使用 unicodedata 模块判断以下字符是否为数字：
阿拉伯语 5：'٥'
泰语 2：'๒'
中文数字：'四'

Python isdigit() 方法检测字符串是否只由数字组成。
Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。

'''

import unicodedata


def is_number(data):
    try:
        float(data)
        print(f'{data} 是数字')
        return True
    except ValueError:
        pass

    for i in data:
        try:
            unicodedata.numeric(i)
        except (TypeError, ValueError):
            break
    else:
        print(f'{data} 是数字')
        return True

    print(f'{data} 不是数字')
    return False


if __name__ == '__main__':
    # 测试字符串和数字
    is_number('foo')
    is_number('1')
    is_number('1.3')
    is_number('-1.37')
    is_number('1e3')

    # 测试 Unicode
    # 阿拉伯语 5
    is_number('٥')
    # 泰语 2
    is_number('๒')
    # 中文数字
    is_number('四五六')
    # 版权号
    is_number('©')