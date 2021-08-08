# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 9/22/2020 3:28 PM
# __software__ : PyCharm

import time
import asyncio
from aiohttp import web


routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Welcome to YiXuan Index!</h1>', content_type='text/html')

@routes.get('/hello')
async def hello(request):
    await asyncio.sleep(0.5)
    return web.Response(text="hello, world")

async def initWebApp(loop):
    app = web.Application()
    app.add_routes(routes)
    srv = await loop.create_server(app._make_hander(), '127.0.0.1', 666)
    web.run_app(app)


if __name__ == '__main__':
    initWebApp()

