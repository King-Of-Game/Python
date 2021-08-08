#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/29/2020 2:44 PM
# __software__ : PyCharm
import asyncio
import aioredis


'''示例1'''


async def execute(address, password):
    print('开始执行', address)
    # 网络IO操作，创建redis 连接
    redis = await aioredis.create_redis(address, password=None)

    # 网络IO操作，在redis中设置哈希值car,, 内部再设三个键值对，
    # 即：redis = { car: {key1:1, key2:2, key3:3} }
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    # 网络IO操作，去redis中获取值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    redis.close()

    # 网络IO操作，关闭redis连接
    await redis.wait_closed()

    print('结束', address)


if __name__ == '__main__':
    asyncio.run(execute('redis://127.0.0.1:6379', '123456'))


'''示例2'''


async def execute(address, password):
    print('开始执行', address)
    # 网络IO操作，创建redis 连接
    redis = await aioredis.create_redis(address, password=None)

    # 网络IO操作，在redis中设置哈希值car,, 内部再设三个键值对，
    # 即：redis = { car: {key1:1, key2:2, key3:3} }
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    # 网络IO操作，去redis中获取值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    redis.close()

    # 网络IO操作，关闭redis连接
    await redis.wait_closed()

    print('结束', address)


async def main():
    task_list = [
        execute('redis://127.0.0.1:6379', None),
        execute('redis://ip:6379', '123456'),
    ]
    await asyncio.wait(task_list)


if __name__ == '__main__':
    asyncio.run(main())
