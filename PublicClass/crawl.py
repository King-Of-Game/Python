# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/24/2019 7:10 PM
# __software__ : PyCharm

import requests
import lxml.html

class Crawler:
    # 初始化类的属性
    def __init__(self, url):

        '''
            爬虫需要的字段https://www.xxx.html
        '''
        self.url = url
        self.headers = {
            'Referer': 'http://www.yhdongman.com/show/21129-37287-0.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        }

    # 得到未经筛选的内容
    def getHtml(self):
        response = requests.get(url=self.url, headers=self.headers)
        response.encoding = 'utf-8'
        html = response.text
        # print(html)
        return html

    # 筛选数据
    def filtrateData(self, data, rule):
        select = lxml.html.document_fromstring(data)
        dataList = select.xpath(rule)
        return dataList
