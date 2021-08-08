#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/23/2020 7:42 PM
# __software__ : PyCharm

from lxml import etree
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi/1.html'
    page_content = requests.get(url, headers).text
    # 实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.HTML(page_content)
    data = tree.xpath('//div[@class="chapter_content"]//text()')
    # data = tree.xpath('//a/@href')
    print(data)
