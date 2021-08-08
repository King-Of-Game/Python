#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/4/2020 7:31 PM
# __software__ : PyCharm

import asyncio
import time


async def request(url):
    print('正在请求url: ', url)
    # 在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
    # time.sleep(2)

    # 当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('请求成功,', url)



if __name__ == '__main__':
    urls = [
        'www.baidu.com',
        'www.sogou.com',
        'www.goubanjia.com'
    ]
    start_time = time.time()

    # 任务列表：存放多个任务对象
    # tasks = []
    # for url in urls:
    #     coroutine = request(url)
    #     task = asyncio.ensure_future(coroutine)
    #     tasks.append(task)

    tasks = [request(url) for url in urls]
    print(tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    end_time = time.time() - start_time
    print('总共用时：%.5f' % end_time)
