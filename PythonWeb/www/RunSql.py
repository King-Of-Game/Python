#!/usr/bin/python3
# _*_ coding: utf-8 _*_
__author__ = 'YiXuan'

import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='123', db='awesome')
    u = User(name='Test', email='871437338@qq.com', passwd='zx454049162~', image='about:blank')
    await u.save()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()