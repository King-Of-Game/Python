#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/28/2020 3:02 PM
# __software__ : PyCharm


import asyncio


class Reader(object):
    ''' 自定义异步迭代器（同时也是异步可迭代对象） '''

    def __init__(self):
        self.count = 0

    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


async def main():
    obj = Reader()
    async for item in obj:
        print(item)


if __name__ == '__main__':
    asyncio.run(main())
