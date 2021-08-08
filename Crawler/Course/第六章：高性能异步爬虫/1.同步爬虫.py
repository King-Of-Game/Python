#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/31/2020 2:47 PM
# __software__ : PyCharm

import requests
import re
import os

urls = [
    'https://www.69shu.org/book/115953/44730109.html',
    'https://www.69shu.org/book/115953/44730110.html',
    # 'https://www.69shu.org/book/115953/44730111.html',
]

def get_response(url):
    print('正在爬取url%s' % url)
    Session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    # get方法是一个阻塞的方法
    response = Session.get(url=url, headers=headers)
    if response.status_code == 200:
        return response
    print(url, '请求失败！')

# 正则处理页面内容
def parse_page_text(response):
    page_text = response.text
    # print(page_text)
    # 正则抓取小说章节名称
    pattern = re.compile('<h1 class="h1title">(.*?)</h1>')
    title = pattern.findall(page_text)[0]

    # 正则抓取小说内容
    pattern1 = re.compile('<div id="htmlContent" .*?</a>.*?<br><br>(.*?)</div>')
    result1 = pattern1.findall(page_text)[0]

    # 正则把<br>或者<br />替换成\n
    pattern2 = re.compile('<br />|<br>')
    result2 = pattern2.sub('\n', result1)

    # 正则把<br>或者<br />替换成\n
    pattern3 = re.compile('&nbsp;')
    result3 = pattern3.sub(' ', result2)

    # result1 = result.replace('<br />', '\n')
    # result2 = result1.replace('&nbsp;', ' ')

    current_chapter = title + '\n\n' + result3 + '\n\n'

    return current_chapter


if __name__ == '__main__':
    if not os.path.exists('./万古第一神.txt'):
        fp = open('./万古第一神.txt', 'w', encoding='utf-8')
        fp.close()

    for url in urls:
        response = get_response(url)
        current_chapter = parse_page_text(response)
        with open('./万古第一神.txt', 'a') as fp:
            fp.write(current_chapter)
