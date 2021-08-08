#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/22/2021 2:28 PM
# __software__ : PyCharm

from multiprocessing import Process


def process_work(count):
    print(f"第 {count} 个进程正在执行")


if __name__ == '__main__':
    print('我是主进程')

    pro = Process(target=process_work,  args=(1,), name='我是进程demo')
    pro.start()




