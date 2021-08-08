#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 3:07 PM
# __software__ : PyCharm

'''
使用random模块生成随机数
'''

import random


# 生成 0 ~ 9 之间的随机数
def zero_to_nine_random():
    ranNum = random.randint(0, 9)   # 返回整数[0, 9]（闭区间）
    return ranNum


if __name__ == '__main__':
    print(zero_to_nine_random())
