#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/20/2021 1:12 PM
# __software__ : PyCharm


# 计算某天是某一年的第几天
def countDays():
    year = int(input('请输入年:'))
    month = int(input('请输入月:'))
    day = int(input('请输入天:'))
    days = day
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_list[1] = 29
    while i < month - 1:
        days += month_list[i]
        i += 1
    print(f'这一天是该年的第 {days} 天')


if __name__ == '__main__':

    countDays()