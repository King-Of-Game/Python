#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/24/2020 1:30 PM
# __software__ : PyCharm

import aiohttp
import asyncio
import os


async def fetch(session, url, index):
    print('发送请求：', url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = './images/cat%d.jpg' % (index + 1)
        with open(file_name, 'wb') as file_object:
            file_object.write(content)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://preview.qiantucdn.com/weitu/75/61/90/24G58PICk6YyAJqMN7IaU_PIC2018.jpg!qt324new_nowater',
            'https://preview.qiantucdn.com/weitu/19/08/25/64p58PICdzfqApIy7Fn2t_PIC2018.jpg!qt324new_nowater',
            'https://img95.699pic.com/photo/50060/5561.jpg_wh860.jpg!/both/324x432/unsharp/true'
        ]
        tasks = [asyncio.create_task(fetch(session, url, url_list.index(url))) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    if not os.path.exists('./images'):
        os.mkdir('images')
    asyncio.run(main())







