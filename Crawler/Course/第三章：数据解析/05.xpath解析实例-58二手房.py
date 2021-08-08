#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/23/2020 11:09 PM
# __software__ : PyCharm

from lxml import etree
import requests


if __name__ == '__main__':
    url = 'https://gz.58.com/ershoufang'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    page_text = requests.get(url, headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('58.txt', 'w', encoding='utf8')
    for li in li_list:
        title = li.xpath('.//h2/a/text()')[0]
        # fp.write(title + '\n')
        print(title)
    fp.close()