#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/30/2020 3:43 PM
# __software__ : PyCharm
import asyncio

import uvicorn
import aioredis
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()

REDIS_POOL = aioredis.ConnectionsPool('redis://127.0.0.1:6379', password=None, minsize=1, maxsize=10)


@app.get('/')
def index():
    '''普通操作接口'''
    return {'message': 'hello world!'}


@app.get('/red')
async def red():
    '''异步操作接口'''

    print('请求来了')
    await asyncio.sleep(1)

    # 连接池获取一个连接
    conn = await REDIS_POOL.acquire()
    redis = Redis(conn)

    # 设置值
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    # 设置值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    # 连接归还连接池
    REDIS_POOL.release(conn)

    return result

if __name__ == '__main__':
    uvicorn.run('yixuanFastAPI:app', host='127.0.0.1', port=5000, log_level='info')
