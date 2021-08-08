#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/30/2020 4:28 PM
# __software__ : PyCharm
import aiohttp
import asyncio


async def fetch(session, url, index):
    print('发送请求：', url)
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text()
        print('第%d个url: %s 得到结果:\n%s' % (index+1, url, len(text)))
        return response.status


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://python.org',
            'https://www.baidu.com',
            'https://www.pythonav.com'
        ]
        tasks = [fetch(session, url, url_list.index(url)) for url in url_list]
        done, pending = await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
