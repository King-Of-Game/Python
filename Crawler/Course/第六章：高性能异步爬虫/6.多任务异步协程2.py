#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/4/2020 10:05 PM
# __software__ : PyCharm

import asyncio
import requests
import time


async def get_page(url):
    print('正在下载', url)
    # requests.get是基于同步，必须使用基于异步的网络请求模块进行指定Url的请求发送
    # aiohttp:基于异步网络请求的模块
    response = requests.get(url)
    print('下载完毕：', response.text)



if __name__ == '__main__':
    start_time = time.time()
    urls = [
        'http://127.0.0.1:5000/yixuan',
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/tom',
    ]


    tasks = [get_page(url) for url in urls]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end_time = time.time()
    print('总共耗时：%.5f' % end_time - start_time)
