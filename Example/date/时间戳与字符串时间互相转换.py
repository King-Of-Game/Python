#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/22/2021 3:56 PM
# __software__ : PyCharm

'''

给定一个时间戳，将其转换为指定格式的时间。

注意时区的设置。

'''

import time
import datetime


# 得到当前时间的时间戳
def getTimeStamp():
    time_stamp = int(time.time())  # 获取当前时间的时间戳
    # print(time_stamp)
    return time_stamp


# 得到当前时间的时间戳
def getTimeStamp1():
    now_time = datetime.datetime.now()  # 得到当前时间
    time_stamp = int(time.mktime(now_time.timetuple()))  # mktime() 方法只能接收元组对象
    # print(time_stamp)
    return time_stamp


# 得到指定时间的时间戳
def getTimeStamp2():
    date_time = '2021-01-22'
    time_tuple = time.strptime(date_time, '%Y-%m-%d')
    print(time_tuple)

    '''
    time_tuple = time.struct_time(
    tm_year=2021, tm_mon=1, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=22, tm_isdst=-1)
    '''

    time_stamp = int(time.mktime(time_tuple))
    print(f"{date_time} 对应的时间戳为: {time_stamp}")


# 根据时间戳得到日期并指定格式
def getStyleTimeFromStamp(time_stamp):
    # .localtime() 方法把时间戳转换为时间元组对象
    time_tuple = time.localtime(time_stamp)

    string_date = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
    print(f"时间戳 {time_stamp} 对应的时间为: {string_date}")


# 根据时间戳得到日期并指定格式
def getStyleTimeFromStamp1(time_stamp):
    # .utcfromtimestamp() 方法把时间戳转换为 datetime 对象
    date_time = datetime.datetime.utcfromtimestamp(time_stamp)

    string_date = date_time.strftime("%Y/%m/%d %H:%M:%S")
    print(f"时间戳 {time_stamp} 对应的时间为: {string_date}")


# 结构化时间和时间戳相互转化
def test():
    now_time = datetime.datetime.today()
    print(f'原始时间: {now_time}')

    strf_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    print(f'格式化时间: {strf_time}')

    struct_time = time.strptime(strf_time, '%Y-%m-%d %H:%M:%S')
    print(f'结构化时间: {struct_time}')
    time_stamp = int(time.mktime(struct_time))
    print(f'得到时间戳: {time_stamp}')

    print('--------------------------------')

    time_stamp = time.time()
    print(f'得到时间戳: {time_stamp}')
    struct_time = time.localtime(time_stamp)
    print(f'结构化时间: {struct_time}')
    strf_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
    print(f'格式化时间: {strf_time}')


if __name__ == '__main__':
    # getTimeStamp()
    # getTimeStamp1()
    # getTimeStamp2()
    #
    # time_stamp = getTimeStamp()
    # print(f"当前时间对应的时间戳: {time_stamp}")
    #
    # getStyleTimeFromStamp(time_stamp)
    # getStyleTimeFromStamp1(time_stamp)

    test()

