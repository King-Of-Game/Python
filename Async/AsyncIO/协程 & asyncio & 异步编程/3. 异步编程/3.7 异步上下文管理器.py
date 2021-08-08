#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/28/2020 8:45 PM
# __software__ : PyCharm

import asyncio


class AsyncContextManager:
    def __init__(self):
        self.conn = conn

    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步连接数据库
        # self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库连接
        await asyncio.sleep(1)


async def main():
    '''方式一：'''
    # obj = AsyncContextManager()
    # async with obj:
    #     pass
    '''
    方式二：
    只有构造类时使用了 __aenter__() 和 __aexit__() 方法才能使用 with ... as ...
    '''
    async with AsyncContextManager() as obj:
        result = await obj.do_something()
        print(result)


if __name__ == '__main__':
    asyncio.run(main())


