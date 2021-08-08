#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/30/2020 1:35 PM
# __software__ : PyCharm

import requests


if __name__ == '__main__':
    Session = requests.Session()
    http_url = 'http://icanhazip.com'
    https_url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'Connection': 'keep-alive'
    }
    proxy = {
        'http': '183.166.138.190:9999',
    }

    response = Session.get(url=http_url, headers=headers, proxies=proxy)
    page_text = response.text
    print(page_text)
    with open('./ip.html', 'w', encoding='utf8') as fp:
        fp.write(page_text)