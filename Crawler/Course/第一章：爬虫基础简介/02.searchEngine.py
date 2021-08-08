#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/7/2020 10:38 PM
# __software__ : PyCharm

import requests


if __name__ == '__main__':
    # url = 'https://www.baidu.com/s'
    url = 'https://www.sogou.com/web'
    kw = input('Please Enter A Key Word:')
    param = {
        # 'wd': kw
        'query':kw
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    response = requests.get(url=url, params=param, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    print(page_text)

