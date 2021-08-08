#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/14/2020 10:05 PM
# __software__ : PyCharm

import requests
import re
import os

def crawlImages(url, headers, pageNum):
    page_text = requests.get(url=url, headers=headers).text

    # 方法一：
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_list = re.findall(ex, page_text, re.S)
    # print(img_list)

    # 方法二：
    # p1 = re.compile('//.*?pictures.*?.(?:jpg|png|gif)')
    # img_list = p1.findall(page_text)
    # # print(img_list)

    for src in img_list:
        img_url = 'https:' + src
        img_data = requests.get(url=img_url, headers=headers).content
        img_name = img_url.split('/')[-1]
        img_path = './images/' + img_name
        with open(img_path, 'wb') as f:
            f.write(img_data)
            print(img_name, '下载成功！')

    print('第%d页爬取的图片数量：%d' % (pageNum, len(img_list)))
    return len(img_list)


if __name__ == '__main__':
    # https://www.qiushibaike.com/

    if not os.path.exists('./images'):
        os.mkdir('./images')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }

    all_imgNum = 0  # 所有图片数量
    # 通用url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'

    for pageNum in range(1, 3):
        new_url = format(url % pageNum)
        all_imgNum += crawlImages(new_url, headers, pageNum)
    print('所有图片数量：%d' % all_imgNum)
