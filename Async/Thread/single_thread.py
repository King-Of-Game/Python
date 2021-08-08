#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/22/2021 3:20 PM
# __software__ : PyCharm

from threading import Thread
import threading
import time


def song(a,b,c):
    print(a, b, c)
    for i in range(5):
        print("song")
        time.sleep(1)


def thread_work(count):
    print(f"第 {count} 个线程程正在执行")


if __name__ == "__main__":
    # 1、使用元组传递 threading.Thread(target=方法名，args=（参数1,参数2, ...）)
    thread = Thread(target=thread_work, args=(1,), name='我是线程demo')
    thread.start()


    # 2、使用字典传递 threading.Thread(target=方法名, kwargs={"参数名": 参数1, "参数名": 参数2, ...})
    # Thread(target=song, kwargs={"a": 1, "c": 3, "b": 2}).start()  # 参数顺序可以变

    # 3、混合使用元组和字典 threading.Thread(target=方法名，args=（参数1, 参数2, ...）, kwargs={"参数名": 参数1,"参数名": 参数2, ...})
    # Thread(target=song, args=(1,), kwargs={"c": 3, "b": 2}).start()