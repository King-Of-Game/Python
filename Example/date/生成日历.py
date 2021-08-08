#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/17/2021 1:15 PM
# __software__ : PyCharm

'''

使用内置模块：calendar 生成日历

'''

import calendar


# 生成日历
def generateCalender():
    while True:
        input_txt = input('***日历（输入q退出）***\n:')
        if input_txt in ['q', 'Q']:
            break

        try:
            year = int(input('请输入年份: '))
            month = int(input('请输入月份: '))

            # 显示日历
            print(calendar.month(year, month))
        except ValueError:
            print('请输入合法的年份和月份！')


if __name__ == '__main__':
    generateCalender()
