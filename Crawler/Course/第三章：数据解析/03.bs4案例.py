#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/22/2020 3:35 PM
# __software__ : PyCharm

from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi/%d.html'
    # title_list = []
    # text_list = []
    fp = open('./sanguo.txt', 'w', encoding='utf8')
    for pageNum in range(1, 3):
        new_url = format(url % pageNum)
        page_text = requests.get(new_url, headers).text
        soup = BeautifulSoup(page_text, 'lxml')
        title = soup.select('#main_left h1')[0].text
        # title_list.append(title)
        content = soup.find('div', class_='chapter_content').text
        # text_list.append(content)
        fp.write(title + ':' + content + '\n')

    fp.close()






