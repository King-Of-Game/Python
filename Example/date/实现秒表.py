#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/19/2021 9:30 PM
# __software__ : PyCharm

'''

使用内置模块 time 实现秒表

'''
import time


def stopWatch():
    input('按下回车键开始，按下 Ctrl + C 停止计时：')
    start_time = time.time()
    print('time starts...')

    try:
        while True:
            time.sleep(1)
            print(f'{round(time.time() - start_time, 0)} secs')
    except KeyboardInterrupt:
        print('time end!')
        end_time = time.time()
        print(f'total time: {round(end_time - start_time, 2)} secs')


if __name__ == '__main__':
    stopWatch()