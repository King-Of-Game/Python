#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/25/2021 2:11 PM
# __software__ : PyCharm

import re


def replaceStr():
    phone = "2004-959-559 # 这是一个电话号码"

    # 删除注释
    num = re.sub(r'#.*$', "", phone)
    print("电话号码 : ", num)

    # 移除非数字的内容
    num = re.sub(r'\D', "", phone)
    print("电话号码 : ", num)


def replaceStr1():
    # 将匹配的数字乘于 2
    def double(matched):
        value = int(matched.group('value'))
        return str(value * 2)

    s = 'A23G4HFD567'

    print(re.sub('(?P<value>\d+)', double, s))  # 大写的P 是用来匹配 <value>, 使matched.group('value')可以识别 value 。
    # print(re.sub('(?P<value>\d)', double, s, count=1))  # A43G4HFD567


if __name__ == '__main__':
    # replaceStr()
    replaceStr1()