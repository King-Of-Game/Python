#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/11/2020 8:35 PM
# __software__ : PyCharm

import requests
import json

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    id_list = []  # 存储企业的id
    all_data_list = []  # 存储所有企业的详细数据
    for i in range(1, 7):
        page = str(i)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        id_json = requests.post(url=url, data=data, headers=headers).json()
        for dic in id_json['list']:
            id_list.append(dic['ID'])

    # 获取企业详情数据
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for i in id_list:
        data = {
            'id': i
        }
        detail_json = requests.post(url=url, data=data, headers=headers).json()
        all_data_list.append(detail_json)
    fp = open('cosmetics.json', 'w', encoding='utf8')
    json.dump(all_data_list, fp, ensure_ascii=False)
    print('crawl over!!!')
