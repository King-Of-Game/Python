#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/25/2020 8:22 PM
# __software__ : PyCharm

from lxml import etree
import requests
import os


if __name__ == '__main__':
    url = 'http://data.acmr.com.cn/member/city/city_md.asp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    page_text = requests.get(url, headers).text
    page_text = page_text.encode('iso-8859-1').decode('gbk')
    tree = etree.HTML(page_text)
    tab_list = tree.xpath('//table[@width="618"]/tr[2]/td/table')

    fTxt = open('./cityName.txt', 'w', encoding='utf-8')
    for tab in tab_list:
        tr_list = tab.xpath('./tbody/tr')
        for i in range(2, len(tr_list)-1):
            tr = tr_list[i]
            td = tr.xpath('./td/text()')
            for cityName in td:
                cityName = cityName.replace(' ','')
                fTxt.write(cityName)
    fTxt.close()





