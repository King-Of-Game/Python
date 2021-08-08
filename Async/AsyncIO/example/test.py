#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/23/2020 7:53 PM
# __software__ : PyCharm
import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其它任务
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其它任务
    print(4)


async def main():
    tasks = [
        asyncio.ensure_future(func1()),
        asyncio.ensure_future(func2()),
    ]
    await asyncio.wait(tasks)


async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'


async def func():
    print('执行协程函数内部代码')

    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行，当前协程挂起时，事件循环可以去执行其它协程（任务）

    response1 = await others()
    print('IO请求结束，结果为：', response1)

    # response2 = await others()
    # print('IO请求结束，结果为：', response2)


if __name__ == '__main__':

    asyncio.run(func())
