#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/7/2020 10:39 PM
# __software__ : PyCharm


import requests
import json

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    word = input('Please Enter Content:')
    data = {
        'kw': word
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    response = requests.post(url=url, data=data, headers=headers)
    jsonObj = response.json()  #json方法返回的是obj(如果确认响应数据是json类型，才可以使用json())
    result = jsonObj['data'][0]
    print(result)
    # 持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'a', encoding='utf8')
    json.dump(jsonObj, fp=fp, ensure_ascii=False)  # 因为中文不能转化为ascii码，所以为False
    fp.close()