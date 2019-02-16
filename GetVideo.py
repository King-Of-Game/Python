#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from multiprocessing import Pool

def temp(i):
    if i < 1000:
        url = "https://cdn1.chlpdq.com/20180906/2lQthu8i/800kb/hls/1P9Vmw92550%03d.ts" % i  # 三个0填充
    else:
        url = "https://cdn1.chlpdq.com/20180906/2lQthu8i/800kb/hls/1P9Vmw92550%04d.ts" % i

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }
    r = requests.get(url=url, headers=headers)
    print(url)
    # print(r.content) # .content 返回的是二进制数据 .text 返回的是字符串
    if i < 1000:
        with open('./mp4/{}'.format(url[-12:]), 'wb') as f:
            f.write(r.content)
    else:
        with open('./mp4/{}'.format(url[-13:]), 'wb') as f:
            f.write(r.content)





if __name__ == '__main__':
    pool = Pool(30)
    for i in range(2200):
        pool.apply_async(temp, (i,))# 创建一个进程
    pool.close()
    pool.join() # 加上这个就是让子进程结束，主进程才会结束。

# #D:\Python练习\mp4>copy /b *.ts abc.mp4

