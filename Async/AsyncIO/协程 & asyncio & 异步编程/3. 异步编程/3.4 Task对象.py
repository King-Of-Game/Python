#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/26/2020 2:51 PM
# __software__ : PyCharm
import asyncio


'''
示例1
'''


# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return '返回值'
#
#
# async def main():
#     print('main start...')
#
#     # 创建Task对象，将当前执行func函数任务添加到事件循环
#     task1 = asyncio.create_task(func())
#     # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）
#     task2 = asyncio.create_task(func())
#     task_list = [
#         func(),
#         func()
#     ]
#
#     print('main end...')
#
#     # 当执行某协程遇到IO操作是，会自动话化切换执行其它任务
#     # 此处的await是等待向对应的协程全部执行完毕并获取结果
#     result1 = await task1
#     result2 = await task2
#     print(result1, result2)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


'''
示例2(推荐✔)
'''


async def func():
    print(1)
    await asyncio.sleep(1)
    print(2)
    return '返回值'


async def main():
    print('main start...')

    task_list = [
        # asyncio.ensure_future(func(), ),  # Python 3.7 之前 ensure_future
        # asyncio.ensure_future(func(), )
        asyncio.create_task(func(), ),    # Python 3.7 之后 create_task
        asyncio.create_task(func(), )
    ]

    print('main end...')

    # 这里之所以不是 asyncio.run(asyncio.wait(...))，是因为 asyncio.run() 函数已经被调用了
    done, pending = await asyncio.wait(task_list, timeout=None)  # timeout=None: 默认等到所有任务执行完成
    print(f'done: {done}\ntype of done: {type(done)}')
    print(f'pending: {pending}')

    result1 = list(done)[0]
    print(f"")
    print(result1)


if __name__ == '__main__':
    asyncio.run(main())

'''
示例3
'''


# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return '返回值'
#
#
# if __name__ == '__main__':
#
#     task_list = [
#         func(),
#         func()
#     ]
#
#     done,pending = asyncio.run(await asyncio.wait(task_list))
#     print(f'done: {done}')
#     print(f'pending: {pending}')
#     return_value = list(done)[0].result()



