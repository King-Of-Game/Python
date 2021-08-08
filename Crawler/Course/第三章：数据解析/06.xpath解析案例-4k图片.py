#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/24/2020 8:04 PM
# __software__ : PyCharm

from lxml import etree
import requests
import os


if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    page_text = requests.get(url, headers).text
    tree = etree.HTML(page_text)
    img_list = tree.xpath('//div[@class="slist"]/ul/li/a/img/@alt')

    if not os.path.exists('./images'):
        os.mkdir('./images')

    for img in img_list:

        img_src = 'http://pic.netbian.com' + img.xpath('./@src')[0]
        img_content = requests.get(url=img_src, headers=headers).content
        # 处理中文乱码：
        imgName = img.xpath('./@alt')[0].encode('iso-8859-1').decode('gbk') + '.jpg'
        with open('./images/' + imgName, 'wb') as fp:
            fp.write(img_content)
            print(imgName + '\t爬取完成')
