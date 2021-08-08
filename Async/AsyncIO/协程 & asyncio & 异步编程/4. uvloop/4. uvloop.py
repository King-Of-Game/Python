#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 11/29/2020 12:42 PM
# __software__ : PyCharm


'''

uvloop（第三方模块）：asyncio 的事件循环的替代方案
作用：
uvloop事件循环的效率大于 asyncio 默认的事件循环
安装：
pip3 install uvloop

* 暂不支持windows

'''


import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# 编写asyncio的代码，与之前写的代码一致
...

# 内部的事件循环自动化会变为uvloop
asyncio.run(...)