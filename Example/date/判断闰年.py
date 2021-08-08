#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/15/2021 5:46 PM
# __software__ : PyCharm

'''

以下两种情况是闰年：
1. 闰年能被 4 整除不能被 100 整除
2. 闰年能被 400 整除

'''


def is_leapYear():
    while True:
        try:
            year = int(input('请输入年份：'))
        except ValueError:
            print('请输入正确的年份！\n')
            continue

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f'{year}是闰年！')
                    break
            else:
                print(f'{year}是闰年！')
                break
        print(f'{year}不是闰年！\n')


if __name__ == '__main__':
    is_leapYear()