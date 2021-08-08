#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/4/2020 10:54 PM
# __software__ : PyCharm

# 使用aiohttp模块中的ClientSession
import asyncio
import requests, aiohttp
import time


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # get(headers, params, proxy='http://ip:port') # 这里代理只能用字符串不能用字典类型
        # post(headers, data, proxy='http://ip:port') # 这里代理只能用字符串不能用字典类型
        async with session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回二进制形式的响应数据
            # json()返回json对象
            # 注意：在异步请求中，只要碰到要等待的代码就要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)
            print(type(page_text))



if __name__ == '__main__':
    start_time = time.time()
    urls = [
        'http://127.0.0.1:5000/yixuan',
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/tom',
    ]

    # tasks = []
    # for url in urls:
    #     coroutine = get_page(url)
    #     task = asyncio.ensure_future(coroutine)
    #     tasks.append(task)

    tasks = [get_page(url) for url in urls]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end_time = time.time()
    print('总共耗时：%.5f' % float(end_time - start_time))
