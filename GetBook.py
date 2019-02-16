#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import lxml.html
from multiprocessing import Pool


# 得到当前页面的文本信息
def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    data = response.text
    return data

# 得到每一章的章节名
def evertTitle(data):
    # 利用document_fromstring方法获取字符串的内容，才能利用xpath方法解析
    select = lxml.html.document_fromstring(data)
    title = select.xpath('//div[@class="entry-tit"]/h1/text()')
    return title

# 得到每一章的内容
def evertText(data):
    select = lxml.html.document_fromstring(data)
    text = select.xpath('//div[@class="m-post"]/p/text()')
    return text


# 拼接章节名和内容
def joinText():
    allText = ""
    # 这里循环的范围是这本小说有多少章（第一章上，第一章中，第一章下：算三章看。具体有多少章，打开网站看第一章和最后一章的网址）
    for i in range(1, 200):
        url = 'http://www.doupobook.com/doupo/%d.html' % i
        print(url)
        data = getData(url)
        allText += "\n%s\n\n" % evertTitle(data)[0]
        Length = len(evertText(data))
        for i in range(Length):
            allText += "%s\n" % evertText(data)[i]
    return allText

# 得到书本
def getBook():
    # 编码为字节类型
    allText = joinText().encode('GBK')
    # 解码为字符串
    allText = allText.decode('GBK')
    with open('斗破苍穹.txt', 'w') as f:
        f.write(allText)





if __name__ == '__main__':
    getBook()








    # pool = Pool(30)
    # for i in range(10):
    #     pool.apply_async(getBook, (i,))# 创建一个进程
    # pool.close()
    # pool.join() # 加上这个就是让子进程结束，主进程才会结束。












