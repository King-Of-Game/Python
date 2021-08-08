#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import lxml.html
import csv

url = 'https://movie.douban.com/top250?start={}&filter='

# 得到当前Url的数据，返回类型为string
def getSource(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
    }
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    data = response.read().decode('utf-8')
    return data

# 得到每一个页面对应的数据，用lxml模块解析后把数据存入列表并返回
def everyPage(source):
    select = lxml.html.document_fromstring(source)
    movieList = select.xpath('//div[@class="info"]')
    showList = []
    for i in movieList:
        movieDict = {}
        title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
        otherTitle = i.xpath('div[@class="hd"]/a/span[@class="other"]/text()')[0]
        mainning = i.xpath('div[@class="bd"]/p[@class=""]/text()')[0]
        star = i.xpath('//div[@class="star"]/span[@class="rating_num"]/text()')[0]
        quote = i.xpath('//p[@class="quote"]/span/text()')[0]
        link = i.xpath('div[@class="hd"]/a/@href')[0]

        movieDict['片名'] = ''.join(title + otherTitle)
        movieDict['演职员'] = mainning
        movieDict['评分'] = star
        movieDict['名言'] = quote
        movieDict['链接'] = link
        showList.append(movieDict)
    return showList

# 生成CSV文件
def getCsv(movieList):
    f = open('douban1.csv', 'w', encoding='utf-8', newline='')
    writer = csv.DictWriter(f, fieldnames=['片名', '演职员', '评分', '名言', '链接'])
    writer.writeheader()
    for i in movieList:
        writer.writerow(i)


if __name__ == '__main__':
    movieList = []
    for i in range(10):
        nowUrl = url.format(i*25)  # 循环得到每一个Url
        print(nowUrl)
        source = getSource(nowUrl)  # 循环得到每一个Url的数据
        movieList += everyPage(source)  # 循环累加得到的数据
    print(movieList)
    getCsv(movieList)  # 把数据传入生成CSV文件的方法中





