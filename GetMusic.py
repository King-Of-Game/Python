#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

url = 'http://1251883823.vod2.myqcloud.com/9dae6688vodgzp1251883823/eac880d05285890783036781533/18NS44RnJlwA.mp4'

def temp(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }
    request = requests.get(url=url, headers=header)
    return request.content

if __name__ == '__main__':
    f = open('./mp4/蚁人2.mp4', 'wb')
    f.write(temp(url))

