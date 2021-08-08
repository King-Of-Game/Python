#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/27/2021 10:51 PM
# __software__ : PyCharm

import re


def reSubn():
    phone = "2004-959-559 # 这是一个电话号码"

    result = re.subn(r'#.*$', '', phone)
    print(result)


if __name__ == '__main__':
    reSubn()
