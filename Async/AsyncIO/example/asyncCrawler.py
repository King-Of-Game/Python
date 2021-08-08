# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 9/22/2020 8:13 PM
# __software__ : PyCharm

import time
import aiohttp
import asyncio
from lxml import etree




urls = [
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16488',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16583',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16380',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16911',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16581',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16674',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16112',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/17343',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16659',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16449',
]

sem = asyncio.Semaphore(10)  # 信号量，控制协程数，防止爬的过快

async def getTitle(url, index):
    with(await sem):
        # async with 是异步上下文管理起
        async with aiohttp.ClientSession() as session:
            async with session.request('GET', url) as response:
                html = await response.read()  # 获取bytes类型的数据
                title = etree.HTML(html).xpath('//*[@id="title"]/text()')[0]
                print('第%d个title为：%s' % (index, title))

# 调用方：
def main():
    loop = asyncio.get_event_loop()
    tasks = [getTitle(urls[i], i+1) for i in range(len(urls))]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    start = time.time()
    main()
    print('总耗时：%.5f秒' % float(time.time() - start))
