#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/20/2021 1:04 PM
# __software__ : PyCharm


from datetime import date
from datetime import timedelta  # 时间增量


def getToday():
    today = date.today()
    print(today)
    today = today.strftime("%Y-%m-%d")
    # print(today)
    return today


def getYesterday():
    today = date.today()
    oneDay = timedelta(days=1)
    yesterday = today - oneDay
    print(yesterday)
    return yesterday


# 计算从出生到现在过了多少天
def countDaysFromBirthday():
    birthday = date(2021, 1, 19)
    today = date.today()
    difference_dates = today - birthday
    days = difference_dates.days
    print(days)


# 计算某天是某年的第几天
def countDays():
    date1 = date(2021, 1, 20)
    # today = date.today()
    date2 = date(2021, 1, 1)
    difference_dates = date1 - date2
    days = difference_dates.days
    print(days)


if __name__ == '__main__':
    getToday()
    getYesterday()
    # countDaysFromBirthday()
    # countDays()

