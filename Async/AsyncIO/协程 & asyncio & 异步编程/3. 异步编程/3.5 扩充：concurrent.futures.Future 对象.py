#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/27/2020 1:44 PM
# __software__ : PyCharm


'''示例1'''
# import time
# from concurrent.futures import Future
# from concurrent.futures.thread import ThreadPoolExecutor
# from concurrent.futures.process import ProcessPoolExecutor
#
#
# def func(value):
#     time.sleep(1)
#     print(value)
#
#
# if __name__ == '__main__':
#     # 创建线程池
#     pool = ThreadPoolExecutor(max_workers=5)
#
#     # 或创建进程池
#     # pool = ProcessPoolExecutor(max_workers=5)
#
#     for i in range(10):
#         fut = pool.submit(func, i)  # 虽然最大5个线程，但是循环10次的10个future对象会一起创建成功，但是状态不一样
#         print(fut)  # 打印线程池的Future 对象：5个<Future at xxx state=running>，5个<Future at xxx state=pending>
#
#         # fut = pool.submit(func, i)  # 虽然最大5个线程，但是循环10次的10个future对象会一起创建成功，但是状态不一样
#         # print(fut)  # 打印进程池的Future 对象：1个<Future at xxx state=running>，9个<Future at xxx state=pending>


'''示例2'''
# import time
# import asyncio
# import concurrent.futures
#
#
# def func1():
#     # 某个耗时操作
#     time.sleep(2)
#     return 'OK'
#
#
# async def main():
#     # 获取当前正在运行的loop
#     loop = asyncio.get_running_loop()
#
#     # 第一步：默认先创建一个线程池，再把 fun1() 放入线程池中，
#     # 第二步：（asyncio.warp_future）会把线程池中 fun1() 返回的future 对象转换为 asyncio 的 future 对象
#
#     fut = loop.run_in_executor(None, func1)  # 在协程中中执行不支持协程的函数（默认None，则创建线程池）
#     result = await fut
#     print('default thread pool', result)
#
    # # 以线程池的方式：
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print('current thread pool', result)

#     # 以进程池的方式：
#     with concurrent.futures.ProcessPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, func1)
#         print('current process pool', result)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


'''案例：asyncio + 不支持异步的模块'''

import asyncio
import requests
import concurrent.futures


async def download_image(url, index):
    # 发送网络请求、下载图片（遇到网络下载图片的IO请求、自动话切换到其它任务）
    print('开始下载第%d张图片，url:%s' % (index+1, url))

    loop = asyncio.get_running_loop()

    # requests模块默认不支持异步操作，所以使用线程池来配合实现异步
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
    content = response.content
    print('下载完成！')

    # 将图片保存到本地
    file_name = 'cat%d.jpg' % (index + 1)
    with open(file_name, 'wb') as file_object:
        file_object.write(content)

    # # 以进程池的方式：
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     response = await loop.run_in_executor(pool, requests.get, url)
    #     content = response.content
    #     print('下载完成！')
    #
    #     # 将图片保存到本地
    #     file_name = 'cat%d.jpg' % (index + 1)
    #     with open(file_name, 'wb') as file_object:
    #         file_object.write(content)


async def main():
    url_list = [
        'https://preview.qiantucdn.com/weitu/75/61/90/24G58PICk6YyAJqMN7IaU_PIC2018.jpg!qt324new_nowater',
        'https://preview.qiantucdn.com/weitu/19/08/25/64p58PICdzfqApIy7Fn2t_PIC2018.jpg!qt324new_nowater',
        'https://img95.699pic.com/photo/50060/5561.jpg_wh860.jpg!/both/324x432/unsharp/true'
    ]

    task_list = [download_image(url, url_list.index(url)) for url in url_list]
    await asyncio.wait(task_list)


if __name__ == '__main__':
    asyncio.run(main())




