#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/22/2021 2:53 PM
# __software__ : PyCharm

'''
多进程间共享数据，可以使用 multiprocessing.Value 和 multiprocessing.Array

'''

from multiprocessing import Process
import time


def process_work(count):
    time.sleep(1)
    print(f"第 {count} 个进程正在执行")


if __name__ == '__main__':
    print('我是主进程')

    start = time.time()

    process_list = []
    for i in range(5):
        p = Process(target=process_work, args=(i,))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()

    end = time.time()

    print(f'进程运行了: {end-start:0.2f} s')




