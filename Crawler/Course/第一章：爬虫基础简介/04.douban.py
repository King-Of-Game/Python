#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/8/2020 8:54 PM
# __software__ : PyCharm

import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = 'utf-8'
    result = response.json()
    fp = open('douban.json', 'a', encoding='utf8')
    json.dump(result, fp=fp, ensure_ascii=False)
    fp.close()
