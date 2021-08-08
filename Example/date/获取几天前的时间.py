#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/22/2021 3:31 PM
# __software__ : PyCharm

'''

计算几天前的时间并转换为指定格式

'''

import time
import datetime


def getPreviousTime(now_time):
    three_day_ago = now_time - datetime.timedelta(days=3)   # 三天前的时间
    print(f"三天前的这时候: {three_day_ago}")

    # 转换为时间戳
    # time.mktime() 方法只能接收元组对象
    time_stamp = int(time.mktime(three_day_ago.timetuple()))  # .timetuple() 方法能转换成时间元组对象
    print(f"{three_day_ago} 的时间戳为: {time_stamp}")

    # 转换为其它字符串格式
    other_style_time = three_day_ago.strftime("%Y/%m/%d %H:%M:%S")
    print(f"其它格式: {other_style_time}")


if __name__ == '__main__':
    now_time = datetime.datetime.now()
    print(f'当前时间: {now_time}')

    getPreviousTime(now_time)