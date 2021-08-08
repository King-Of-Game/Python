#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/22/2021 4:08 PM
# __software__ : PyCharm

from threading import Thread
import time


def thread_work(count):
    time.sleep(1)
    print(f"第 {count} 个线程正在执行")


if __name__ == '__main__':
    print('主线程')

    start = time.time()

    thread_list = []
    for i in range(5):
        t = Thread(target=thread_work, args=(i,))
        t.start()
        thread_list.append(t)

    for thread in thread_list:
        thread.join()

    end = time.time()

    print(f'线程一共运行了: {end - start:0.2f} s')
