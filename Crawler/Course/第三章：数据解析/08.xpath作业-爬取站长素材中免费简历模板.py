#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/26/2020 1:42 PM
# __software__ : PyCharm

from lxml import etree
import requests
import os

# 处理中文乱码
def deal_garbled_code(response):
    # response = requests.get(url, headers)
    response.status_code
    response.encoding = response.apparent_encoding
    return response.text


if __name__ == '__main__':
    url = 'http://sc.chinaz.com/jianli/free.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    if not os.path.exists('./rar'):
        os.mkdir('./rar')
    for i in range(1, 2):
        if i > 1:
            url = 'http://sc.chinaz.com/jianli/free_%d.html' % i
        page_text = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page_text)
        url_list = tree.xpath('//div[@id="container"]/div/a/@href')

        for src in url_list:
            print(src)
            response = requests.get(url=src, headers=headers)
            # 处理页面数据中文乱码
            page_text = deal_garbled_code(response)

            tree = etree.HTML(page_text)
            rar_download_url = tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a/@href')[0]
            rar_name = tree.xpath('//h1/text()')[0] + '.rar'
            print(rar_download_url)

            rar_object = requests.get(url=rar_download_url, headers=headers).content
            with open('./rar/' + rar_name, 'wb') as fp:
                fp.write(rar_object)
            print(rar_name, '爬取完成......\n\n')