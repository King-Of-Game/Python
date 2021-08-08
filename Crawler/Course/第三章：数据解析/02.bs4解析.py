#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/20/2020 3:06 PM
# __software__ : PyCharm

import requests
import lxml
from bs4 import BeautifulSoup

def crawlNovel(url,):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    page_text = requests.get(url, headers).text
    # print(page_text)
    return page_text

def dealByBs4(url):
    # 实例化本地html文件
    # fp = open('./test.html', 'r', encoding='utf8')
    # soup = BeautifulSoup(fp, 'lxml')

    page_text = crawlNovel(url)
    soup = BeautifulSoup(page_text, 'lxml')
    print(soup.select('a')[3]['href'])










if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi/%d.html'
    for pageNum in range(1,2):
        url = format(url % pageNum)
        dealByBs4(url)
