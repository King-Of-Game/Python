# 1. 协程

## 1.1 为什么要学协程？

+ 异步非阻塞、asyncio
+ tornado、fastapi、django 3.x asgi、aiohttp -> 都在往异步发展 -> 提升性能

## 1.2 什么是协程？

+ 协程不是由计算机提供，而是程序员人为创造。
+ 协程（coroutine），也可以被称为称为微线程，是一种用户态的上下文切换技术，简而言之，其实就是通过一个线程实现代码块相互切换执行。

## 1.3 实现携程的四种方法

+ greenlet（早期模块）
+ yield关键字
+ asyncio 装饰器（py3.4）
+ async, await关键字（py3.5）【推荐】

### greenlet 

+ pip3 install greenlet

#### 示例

+ ```python
  from greenlet import greenlet
  
  def fun1():
      print(1)		# 第2步：输入 1
      gr2.switch()	# 第3步：切换到 func2 函数
      print(2)		# 第6步：输入 2
      gr2.switch()	# 第7步：切换到 func2 函数
      
  def fun2():
      print(3)		# 第4步：输入 3
      gr1.switch()	# 第5步：切换到 func2 函数
      print(4)		# 第8步：输入 2
      
  gr1 = greenlet(func1)
  gr2 = greenlet(func2)
  gr1.switch()		# 第1步：执行 func1 函数 
  ```

### yield 关键字

#### 示例

+ ```python
  def func1():
      yield 1
      yield from func2()
      yield 2
      
  def func2():
      yield 3
      yield from func1()
      yield 4
      
  if __name__ == '__main__':
      f1 = func1()
      for item in fi:
          print(item)
  ```

### asyncio 装饰器（py3.4）

+ 注意：遇到IO阻塞自动切换

#### 示例

+ ```python
  import asyncio
  
  
  @asyncio.coroutine
  def func1():
      print(1)
      yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其它任务
      print(2)
      
  @asyncio.coroutine
  def func2():
      print(3)
      yield from asyncio.sleep(2)
      print(4)
      
      
  if __name__ == '__main__':
      tasks = [
          asyncio.ensure_future(func1()),
          asyncio.ensure_future(func2()),
      ]
      loop = asyncio.get_event_loop()
      loop.run_until_complete(asyncio.wait(tasks))
  ```

### async & await 关键字（py3.5）

#### 示例

+ ```python
  import asyncio
  
  
  async def fun1():
      print(1)
      await asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其它任务
      print(2)
  
  async def func2():
      print(3)
      await asyncio.sleep(2)
      print(4)
      
      
  if __name__ == '__main__':
      tasks = [
          asyncio.ensure_future(func1()),
          asyncio.ensure_future(func2()),
      ]
      loop = asyncio.get_event_loop()
      loop.run_until_complete(asyncio.wait(tasks))
  ```

# 2. 协程的意义

+ 在一个线程中如何遇到IO等待时间，让线程不会傻傻等着，利用等待的时间再去干其它的事。

## 示例：去下载三张图片（网络IO）

+ 普通方式（同步：排队，一个接一个）

  + ```python
    import requests
    
    def download_image(url):
        print(f"开始下载: {url}")
        # 发送网络请求，下载图片
        response = requests.get(url)
        print("下载完成")
        # 图片保存到本地
        file_name = url.split('_')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(response.content)
            
    if __name__ == '__main__':
        url_list = [
            'https://preview.qiantucdn.com/weitu/75/61/90/24G58PICk6YyAJqMN7IaU_PIC2018.jpg!qt324new_nowater',
     	    'https://preview.qiantucdn.com/weitu/19/08/25/64p58PICdzfqApIy7Fn2t_PIC2018.jpg!qt324new_nowater',
     	    'https://img95.699pic.com/photo/50060/5561.jpg_wh860.jpg!/both/324x432/unsharp/true'  
            ]
        for item in url_list:
            download_image(item)
            
    ```

+ 协程方式（异步：把任务请求发出去而不等待结果，立即执行下个任务）

  + ```python
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
    ```

# 3. 异步编程

## 3.1 事件循环

+ 可以理解成为一个死循环，去检测并执行某些代码。

  + ```python
    # 伪代码
    
    任务列表 = [任务1，任务2，任务3....]    # 任务有很多种状态
    
    while True:
        可执行的任务列表，已完成的任务列表 = 去任务列表中检查所有的任务，将‘可执行’和‘已完成‘的任务返回
        for 就绪任务 in 已准备就绪的任务列表:
              执行已就绪的任务
        for 已完成的任务 in 已完成的任务列表:
              在任务列表中移除 已完成的任务
        如果 任务列表 中的任务都已完成，则终止循环
    ```

  + ```python
    import asyncio
    
    tasks = [task1,task2,task3...]
    # 生成一个事件循环
    loop = asyncio.get_event_loop()
    # 将任务放到 任务列表
    loop.run_until_complete(asyncio.wait(tasks))
    ```

## 3.2 快速上手

+ 协程函数，定义函数的时候：async def 函数名

+ 协程对象，执行 协程函数() 得到的就是协程对象。

  + ```python
    # 定义一个协程函数
    async def fun():
        pass
    
    # 创建一个协程对象（注意：函数内部代码不会执行）
    result = func()
    ```

  + 如果想要运行协程函数内部代码，必须要将协程对象交给事件循环来处理

  + ```python
    import asyncio
    
    async def func():
        print('快来数一数')
    
    result = func()
    
    # 生成一个事件循环
    # loop = asyncio.get_event_loop()
    # 将任务放到 任务列表
    # loop.run_until_complete(result)
    
    asyncio.run(result)  # python3.7版本
    ```

## 3.3 await

+ await 后跟可等待的对象（比如：协程对象、Future、Task对象 -> IO等待）

### 示例1：只存在一个协程函数

+ ```python
  import asyncio
  
  async def func():
      print('hello')
      response = await asyncio.sleep(2)
      print('end', response)
  
  asyncio.run( func() )
  ```

### 示例2：一个协程函数调用另一个协程函数

+ ```python
  import asyncio
  
  async def others():
      
      print('start')
      await asyncio.sleep(2)
      print('end')
      return '返回值'
  
  async def func():
      print('执行协程函数内部代码')
      
      # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行，当前协程挂起时，事件循环可以去执行其它协程（任务）
      response = await others()
      
      print('IO请求结束，结果为：', response)
  
  asyncio.run( func() )
  ```

### 示例3：一个协程函数中可以有多个 await

+ 注意：await 就是拿到等待对象的值得到结果之后再继续向下走。（在等待结果期间会执行其它代码）

+ ```python
  import asyncio
  
  async def others():
      
      print('start')
      await asyncio.sleep(2)
      print('end')
      return '返回值'
  
  async def func():
      print('执行协程函数内部代码')
      
      # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行，当前协程挂起时，事件循环可以去执行其它协程（任务）
      response1 = await others()
      print('IO请求结束，结果为：', response1)
      
      # 这个要等response1返回结果后才能继续执行
      response2 = await others()
      print('IO请求结束，结果为：', response2)
  
  asyncio.run( func() )
  ```

## 3.4 Task对象（并发地调度当前协程对象）

+ Tasks 用于并发调度协程，通过 asyncio.create_task(协程对象) 的方式创建Task对象，这样可以让协程加入事件循环中等待被调度执行，除了使用 asyncio.create_task() 函数以外，还可以用低层级的 loop.create_task() 或 asyncio.ensure_flture() 函数。不建议手动实例化 Task 对象

### 作用

+ 在事件循环中并发地添加多个任务，让事件循环遇到IO能切换到下一个任务

### 注意

+ asyncio.create_task() 函数在 Python3.7 中被加入。在 Python 3.7 之前，可以改用低层级的asyncio.ensure_future() 函数

### 示例1：基础写法

+ ```python
  import asyncio
  
  async def func():
      print(1)
      await asyncio.sleep(2)
      print(2)
      return '返回值'
  
  async def main():
      print('main start...')
  
      # 创建Task对象，将当前执行func函数任务添加到事件循环
      task1 = asyncio.create_task(func())
      # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）
      task2 = asyncio.create_task(func())
  
      print('main end...')
  
      # 当执行某协程遇到IO操作是，会自动话化切换执行其它任务
      # 此处的await是等待向对应的协程全部执行完毕并获取结果
      result1 = await task1
      result2 = await task2
      print(result1, result2)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```

### 示例2：规范写法(推荐✔)

+ ```python
  import asyncio
  
  async def func():
      print(1)
      await asyncio.sleep(2)
      print(2)
      return '返回值'
  
  
  async def main():
      print('main start...')
  
      task_list = [
          # asyncio.ensure_future(func(), ),  # Python 3.7 之前 ensure_future
          # asyncio.ensure_future(func(), )
          asyncio.create_task(func(), ),    # Python 3.7 之后 create_task
          asyncio.create_task(func(), )
      ]
  
      print('main end...')
  	
      # 这里之所以不是 asyncio.run(asyncio.wait(...))，是因为 asyncio.run() 函数已经被调用了
      done, pending = await asyncio.wait(task_list, timeout=None)  # timeout=None: 默认等到所有任务执行完成
      print(done)
      # print(pending)
      
      result1 = list(done)[0].result()
      print(result1)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```

### 示例3：简洁写法

+ ```python
  import asyncio
  
  async def func():
      print(1)
      await asyncio.sleep(2)
      print(2)
      return '返回值'
  
  
  if __name__ == '__main__':
      task_list = [
          func(),  # 使用asyncio.create_task(func()) 会报错：因为事件循环没有被创建，而create_task()方法会立即将协程对象添加到事件循环
          func()
      ]
  
      done,pending = asyncio.run(asyncio.wait(task_list))  # asyncio.run()会先创建一个事件循环，有了事件循环后才能调用asyncio.create_task(func())
      print(done)
      # print(pending)
  
      result1 = list(done)[0].result()
      print(result1)
  ```

## 3.5 asyncio.Future 对象

+ Task继承Future, Task 对象内部 await 结果的处理基于 Future 对象来的

### 说明

+ 一个更低级的接口，帮助我们去等待协程函数的结果

### 示例1：future 对象的基本使用

+ ```python
  import asyncio
  
  
  async def main():
      # 获取当前事件循环
      loop = asyncio.get_running_loop()
  
      # 创建一个任务（Future对象），这个任务什么都不干
      fut = loop.create_future()
  
      # 等待任务最终结果（Future），没有结束则会一直等下去。
      await fut
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```

### 示例2：手动设置 future 任务的最终结果

+ ```python
  import asyncio
  
  
  async def set_after(fut):
      await asyncio.sleep(2)
      fut.set_result('666')
  
  async def main():
      # 获取当前事件循环
      loop = asyncio.get_running_loop()
  
      # 创建一个任务（Future对象），这个任务什么都不干
      fut = loop.create_future()
  
      # 创建一个任务（Task对象），绑定了set_after函数，函数内部再2s之后，会给fut赋值
      # 即手动设置 future 任务的最终结果，那么 fut 就可以结束了
      await loop.create_task(set_after(fut))
  
      # 等待 future 对象获取最终结果，否则一直等待下去
      data = await fut
      print(data)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```

## 3.6 concurrent.futures.Future 对象

### 说明

+ 使用线程池，进程池实现异步操作时用到的对象。
+ 写代码可能会存在交叉使用
+ 例如：CRM 项目80%都是基于协程异步编程 + MySQL（如果MySQL不支持基于协程的异步）【那就用线程、进程做异步编程】

### 示例1：concurrent.futures.Future 对象的基本使用

+ ```python
  import time
  from concurrent.futures import Future
  from concurrent.futures.thread import ThreadPoolExecutor
  from concurrent.futures.process import ProcessPoolExecutor
  
  
  def func(value):
      time.sleep(1)
      print(value)
  
  
  if __name__ == '__main__':
      # 创建线程池
      pool = ThreadPoolExecutor(max_workers=5)
  
      # 或创建进程池
      # pool = ProcessPoolExecutor(max_workers=5)
  
      for i in range(10):
          fut = pool.submit(func, i)  # 虽然最大5个线程，但是循环10次的10个future对象会一起创建成功，但是状态不一样
          print(fut)  # 打印线程池的Future 对象：5个<Future at xxx state=running>，5个<Future at xxx state=pending>
  
          # fut = pool.submit(func, i)  # 虽然最大5个线程，但是循环10次的10个future对象会一起创建成功，但是状态不一样
          # print(fut)  # 打印进程池的Future 对象：1个<Future at xxx state=running>，9个<Future at xxx state=pending>
  ```

### 示例2：在协程中执行不支持协程的函数

+ ```python
  import time
  import asyncio
  import concurrent.futures
  
  
  def func1():
      # 某个耗时操作
      time.sleep(2)
      return 'OK'
  
  
  async def main():
      # 获取当前正在运行的loop
      loop = asyncio.get_running_loop()
  
      # run_in_executor(None, func1)函数内部行为：
      # 第一步：默认先创建一个线程池，再把 fun1() 放入线程池中，
      # 第二步：（asyncio.warp_future）会把线程池中 fun1() 返回的future 对象转换为 asyncio 的 future 对象
  
      fut = loop.run_in_executor(None, func1)  # 可以在协程中执行不支持协程的函数（默认None：表示创建线程池）
      result = await fut
      print('default thread pool', result)
  
      # # 以线程池的方式：
      # with concurrent.futures.ThreadPoolExecutor() as pool:
      #     result = await loop.run_in_executor(pool, func1)
      #     print('current thread pool', result)
      #
      # # 以进程池的方式：
      # with concurrent.futures.ProcessPoolExecutor() as pool:
      #     result = await loop.run_in_executor(pool, func1)
      #     print('current process pool', result)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```

### 示例3：asyncio + 不支持异步的 requests 模块

+ ```python
  import asyncio
  import requests
  
  
  async def download_image(url, index):
      # 发送网络请求、下载图片（遇到网络下载图片的IO请求、自动话切换到其它任务）
      print('开始下载第%d张图片，url:%s' % (index+1, url))
  
      loop = asyncio.get_running_loop()
      # requests模块默认不支持异步操作，所以使用线程池来配合实现异步
      future = loop.run_in_executor(None, requests.get, url)  # 默认使用线程池
      response = await future
      content = response.content
      print('下载完成！')
      
      # 将图片保存到本地
      file_name = 'cat%d.jpg' % (index + 1)
      with open(file_name, 'wb') as file_object:
          file_object.write(content)
          
      # # 以进程池的方式：
      # with concurrent.futures.ProcessPoolExecutor() as pool:
      #     response = await loop.run_in_executor(pool, requests.get, url)
      #     content = response.content
      #     print('下载完成！')
      #
      #     # 将图片保存到本地
      #     file_name = 'cat%d.jpg' % (index + 1)
      #     with open(file_name, 'wb') as file_object:
      #         file_object.write(content)
          
  
  async def main():
      url_list = [
          'https://preview.qiantucdn.com/weitu/75/61/90/24G58PICk6YyAJqMN7IaU_PIC2018.jpg!qt324new_nowater',
          'https://preview.qiantucdn.com/weitu/19/08/25/64p58PICdzfqApIy7Fn2t_PIC2018.jpg!qt324new_nowater',
          'https://img95.699pic.com/photo/50060/5561.jpg_wh860.jpg!/both/324x432/unsharp/true'
      ]
  
      task_list = [download_image(url, url_list.index(url)) for url in url_list]
      await asyncio.wait(task_list)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```

## 3.7 异步迭代器

### 什么是异步迭代器？

+ 实现了 __aiter__() 和 __anext__() 方法的对象。 
+ __anext__ 必须返回一个 awaitable 对象，async_for 会处理异步迭代器的 __anext__() 方法所返回的可等待对象，直到其引发一个 StopAsyncIteration 异常。由PEP_492 引入。

### 什么是异步可迭代对象？

+ 可在 async_for 语句中被使用的对象，必须通过它的 __aiter__() 方法并返回一个 asynchronous_iterator（异步迭代器）。由PEP_492 引入

### 示例1：

+ ```python
  import asyncio
  
  
  class Reader(object):
      ''' 自定义异步迭代器（同时也是异步可迭代对象） '''
  
      def __init__(self):
          self.count = 0
  
      async def readline(self):
          # await asyncio.sleep(1)
          self.count += 1
          if self.count == 100:
              return None
          return self.count
  
      def __aiter__(self):
          return self
  
      async def __anext__(self):
          val = await self.readline()
          if val is None:
              raise StopAsyncIteration
          return val
  
  async def main():
      obj = Reader()
      async for item in obj:
          print(item)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```


## 3.8 异步上下文管理器

+ 此种对象通过定义 __aenter__() 和 __aexit__() 方法来对 async_with 语句中的环境进行控制，由 PEP-492 引入。

```python
import asyncio


class AsyncContextManager:
    def __init__(self):
        self.conn = conn

    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步连接数据库
        # self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库连接
        await asyncio.sleep(1)

async def main():
    '''方式一：'''
    # obj = AsyncContextManager()
    # async with obj:
    #     pass
    '''
    方式二：
    只有构造类时使用了 __aenter__() 和 __aexit__() 方法才能使用 with ... as ...
    '''
    async with AsyncContextManager() as obj:
        result = await obj.do_something()
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
```

# 4. uvloop

+ uvloop是asyncio的事件循环的替代方案。（uvloop的事件循环效率 大于 默认asyncio的事件循环。）

## 注意

+ wsgi: （Python Web Server Gateway Interface）Web服务器网关接口）asgi：支持异步的web服务网关接口一个asgi -> uvicorn（内部使用的就是uvloop）

## 示例

- ```python
  import asyncio
  import uvloop
  asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
  
  
  # 编写asyncio的代码，与之前写的代码一致
  ...
  
  # 内部的事件循环自动化会变为uvloop
  asyncio.run(...)
  ```

# 5. 实战案例

## 5.1 异步redis

+ 在使用 python diamagnetic操作 redis 时，连接/操作/断开都是网络IO。

### 示例1：异步操作单个 redis 连接

+ ```python
  import asyncio
  import aioredis
  
  
  async def execute(address, password):
      print('开始执行', address)
      # 网络IO操作，创建redis 连接
      redis = await aioredis.create_redis(address, password=password)
  
      # 网络IO操作，在redis中设置哈希值car,, 内部再设三个键值对，
      # 即：redis = { car: {key1:1, key2:2, key3:3} }
      await redis.hmset_dict('car', key1=1, key2=2, key3=3)
  
      # 网络IO操作，去redis中获取值
      result = await redis.hgetall('car', encoding='utf-8')
      print(result)
  
      redis.close()
  
      # 网络IO操作，关闭redis连接
      await redis.wait_closed()
  
      print('结束', address)
  
  
  if __name__ == '__main__':
      asyncio.run(execute('redis://127.0.0.1:6379', '123456'))
  ```

### 示例2：异步操作多个 redis 连接

+ ```python
  import asyncio
  import aioredis
  
  
  async def execute(address, password):
      print('开始执行', address)
      # 网络IO操作，创建redis 连接
      redis = await aioredis.create_redis(address, password=None)
  
      # 网络IO操作，在redis中设置哈希值car,, 内部再设三个键值对，
      # 即：redis = { car: {key1:1, key2:2, key3:3} }
      await redis.hmset_dict('car', key1=1, key2=2, key3=3)
  
      # 网络IO操作，去redis中获取值
      result = await redis.hgetall('car', encoding='utf-8')
      print(result)
  
      redis.close()
  
      # 网络IO操作，关闭redis连接
      await redis.wait_closed()
  
  
      print('结束', address)
  
  
  async def main():
      task_list = [
          execute('redis://127.0.0.1:6379', None),
          execute('redis://ip:6379', '123456'),
      ]
      await asyncio.wait(task_list)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```

## 5.2 异步MySQL

### 示例1：异步操作单个 mysql 连接

+ ```python
  import asyncio
  import aiomysql
  
  
  async def execute():
      # 异步IO操作：连接MySQL
      conn = await aiomysql.connect(host='localhost', port=3306, user='root', password='123456', db='test')
  
      # 网络IO操作：创建游标
      cur = await conn.cursor()
  
      # 网络IO操作：执行SQL
      await cur.execute('select * from t_student')
  
      # 网络IO操作：获取SQL结果
      result = await cur.fetchall()
      print(result)
  
      # 网络IO操作：关闭连接
      await cur.close()
      conn.close()
  
  
  def main():
      asyncio.run(execute())
  
  
  if __name__ == '__main__':
      main()
  ```

### 示例2：异步操作多个 mysql 连接

+ ```python
  import asyncio
  import aiomysql
  
  
  async def execute(host, password):
      # 异步IO操作：连接MySQL(遇到IO会自动切换任务)
      conn = await aiomysql.connect(host=host, port=3306, user='root', password=password, db='test')
  
      # 网络IO操作：创建游标(遇到IO会自动切换任务)
      cur = await conn.cursor()
  
      # 网络IO操作：执行SQL(遇到IO会自动切换任务)
      await cur.execute('select * from t_student')
  
      # 网络IO操作：获取SQL结果(遇到IO会自动切换任务)
      result = await cur.fetchall()
      print(result)
  
      # 网络IO操作：关闭连接(遇到IO会自动切换任务)
      await cur.close()
      conn.close()
      print('结束', host)
  
  
  async def main():
      task_list = [
          execute('47.91.42.197', '123456'),
          execute('localhost', '123456')
      ]
      await asyncio.wait(task_list)
  
  
  if __name__ == '__main__':
      asyncio.run(main())
  ```

## 5.3 FastAPI 框架

### 安装模块

+ pip3 install fastapi
+ pip3 install uvicorn (asgi: 内部基于uvloop)

### 示例1：yixuanFastAPI.py

- ```python
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
  ```

## 5.4 异步爬虫 aiohttp

### 安装模块

+ pip3 install aiohttp

### 示例

+ ```python
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
  ```

# 总结

+ 协程最大的意义：通过一个线程利用其IO等待时间去做其它事情。