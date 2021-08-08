#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/8/2020 9:54 PM
# __software__ : PyCharm

import requests
import asyncio
import aiohttp
import json

def kfc(pageIndex):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': pageIndex,
        'pageSize': '10',
    }
    response = requests.post(url=url, data=data, headers=headers)
    response.encoding = 'utf-8'
    result = response.text
    print(result)
    fp = open('kfc.json', 'a', encoding='utf8')
    json.dump(result, fp=fp, ensure_ascii=False)
    fp.close()

async def asyncKfc(pageIndex):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': pageIndex,
        'pageSize': '10',
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, data=data, headers=headers) as request:
            response = request.text()
            print(response)

    # response = requests.post(url=url, data=data, headers=headers)
    # response.encoding = 'utf-8'
    # result = response.text
    # print(result)
    # fp = open('./kfc.json', 'a', encoding='utf8')
    # json.dump(result, fp=fp, ensure_ascii=False)
    # fp.close()

def main():
    tasks = [kfc(i) for i in range(1,8)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    for i in range(1,8):
        kfc(i)

