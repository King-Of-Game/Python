#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/14/2020 10:08 PM
# __software__ : PyCharm

import requests
import re

if __name__ == '__main__':
    url = 'https://pic.qiushibaike.com/system/pictures/12368/123680258/medium/DN5HK36OUG4192ZG.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    img_data = requests.get(url=url, headers=headers).content
    with open('./1.jpg', 'wb') as f:
        f.write(img_data)
