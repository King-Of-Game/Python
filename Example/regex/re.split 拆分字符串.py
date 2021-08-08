#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/27/2021 11:06 PM
# __software__ : PyCharm

import re


def reSplit():
    string = 'apple banana orange'

    result = re.split(r'\s', string)  # 匹配任何空白字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。
    print(result)


if __name__ == '__main__':
   reSplit()
