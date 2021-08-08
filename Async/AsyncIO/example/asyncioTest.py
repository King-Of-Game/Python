# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# __date__ : 2019/10/15 10:11
# __software__ : PyCharm
# @Software: PyCharm

import time
import asyncio


# 子生成器函数
async def add():
    await asyncio.sleep(2)


async def reduce():
    await asyncio.sleep(3)



# 协程（委托生成器）函数
async def taskOne():
    await add()

async def taskMore():
    tasks = [add(), reduce()]
    done, pending = await asyncio.wait(tasks)
    for i in done:
        print('协程无序返回值：' + str(i.result()))



async def test():
    await asyncio.sleep(2)
    print('*' * 20)

async def hello():
    print('hello1')
    await asyncio.sleep(2)
    print('hello2')


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    # tasks = [test(), hello()]  #
    # loop.run_until_complete(asyncio.wait(tasks))  # 多个函数使用：asyncio.wait()
    loop.close()


if __name__ == '__main__':
    start = time.time()
    main()
    print('总共用时：%.5f' % float(time.time() - start))

















