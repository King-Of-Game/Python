#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/3/2020 9:47 PM
# __software__ : PyCharm

import asyncio

async def request(url):
    print('正在请求url: ', url)
    print('请求成功,', url)
    return url

def main(coroutine):
    # 创建一个事件循环对象
    loop = asyncio.get_event_loop()
    # 将协程对象注册到loop中，然后启动loop
    loop.run_until_complete(coroutine)

# task的使用
def main1(coroutine):
    loop = asyncio.get_event_loop()

    task = loop.create_task(coroutine)
    print(task)
    loop.run_until_complete(task)
    print(task)

# future(本质还是一个task)的使用
def main2(coroutine):
    task = asyncio.ensure_future(coroutine)
    loop = asyncio.get_event_loop()

    print(task)
    loop.run_until_complete(task)
    print(task)

# 绑定回调
def callback_func(task):
    # result 返回的就是任务对象中封装的协程对象对应函数的返回值
    print('回调结果：', task.result())

def main3(coroutine):
    loop = asyncio.get_event_loop()
    # task = loop.create_task(coroutine)
    task = asyncio.ensure_future(coroutine)
    # 将回调函数绑定到任务对象中
    task.add_done_callback(callback_func)
    loop.run_until_complete(task)



if __name__ == '__main__':
    url = 'www.baidu.com'
    coroutine = request(url)
    # main(coroutine)
    # main1(coroutine)
    # main2(coroutine)
    main3(coroutine)