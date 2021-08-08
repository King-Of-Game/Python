# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 9/22/2020 10:28 PM
# __software__ : PyCharm

import time
import aiohttp
import asyncio
from lxml import etree
from multiprocessing import Pool, cpu_count

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
            async with session.request('GET', url) as resp:
                html = await resp.read()  # 获取bytes类型的数据
                title = etree.HTML(html).xpath('//*[@id="title"]/text()')[0]
                print('第%d个%s的title为：%s' % (index, url, title))

# 协程调用方：
def aioGetHtml(url, index):
    loop = asyncio.get_event_loop()
    # tasks = [getTitle(urls[i], i+1) for i in range(len(urls))]
    # loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(getTitle(url, index))
    loop.close()


def main():
    p = Pool(10)
    for i in range(len(urls)):
        # p.apply_async(multiParseHtml, args=(htmls[i], i+1))
        p.apply_async(aioGetHtml, args=(urls[i], i + 1))
    p.close()
    p.join()





if __name__ == '__main__':
    # start = time.time()
    # main()
    # print('总耗时：%.5f秒' % float(time.time() - start))


    # def f(x):
    #     return x * x
    #
    #
    # numbers = [1, 3, 6]
    # newNumbers = tuple(map(lambda x: x, numbers))
    # print(newNumbers)
    x = 2
    while x == 2:
        print(x)
    else:
        print(x)
    print('********')
    for i in range(3):
        print(i)
    else:
        print('???')


