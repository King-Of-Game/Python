#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import lxml.html
from multiprocessing import Pool


# 得到当前页面的文本信息
def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.58pic.com',
        'Referer': 'http://www.58pic.com/tupian/jiafeimao-807-0.html',
        'X-Requested-With': 'XMLHttpRequest'

    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    data = response.text
    return data

# 得到图片列表
def imgList(data):
    # 利用document_fromstring方法获取字符串的内容，才能利用xpath方法解析
    select = lxml.html.document_fromstring(data)
    imglist = select.xpath('//div[@class="flow-item qt-card-primary masonry-brick"]')
    print(imglist)
    return imglist


# 保存图片到本地
def getImg(imgList):
    with open('./images/1.jpg', 'wb') as f:
        f.write(imgList)




if __name__ == '__main__':
    search = "jiafeimao"  # 不能为中文
    url = url = 'http://www.58pic.com/tupian/%s-807-0.html' % search
    print(url)
    data = getData(url)
    imgList(data)












    # pool = Pool(30)
    # for i in range(10):
    #     pool.apply_async(getBook, (i,))# 创建一个进程
    # pool.close()
    # pool.join() # 加上这个就是让子进程结束，主进程才会结束。












