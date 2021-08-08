#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/26/2020 9:08 PM
# __software__ : PyCharm

import asyncio


'''示例1'''


# async def main():
#     # 获取当前事件循环
#     loop = asyncio.get_running_loop()
#     # 创建一个任务（Future对象），这个任务什么都不干
#     fut = loop.create_future()
#
#     # 等待任务最终结果（Future），没有结束则会一直等下去。
#     await fut
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


'''示例2'''


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('666')


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个任务（Future对象），这个任务什么都不干
    fut = loop.create_future()

    # 创建一个任务（Task对象），绑定了set_after函数，函数内部再2s之后，会给fut赋值
    # 即手动设置 future 任务的最终结果，那么 fut 就可以结束了
    await loop.create_task(set_after(fut))

    # 等待 future对象获取最终结果，否则一直等待下去
    data = await fut
    print(data)

if __name__ == '__main__':
    asyncio.run(main())




