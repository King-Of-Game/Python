# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/8/13
# https://www.69shu.org/book/17166/7548140.html
import requests
import lxml.html
from multiprocessing import Pool

import os,sys

'''
join()方法：
join()： 连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串。
split():split方法中不带参数时，表示分割所有换行符、制表符、空格。
'''

# 得到当前页面的文本信息
def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'GBK'
    data = response.text
    # print(data)
    return data

# 得到每一章的章节名
def everyTitle(data, condition):
    # 利用document_fromstring方法获取字符串的内容，才能利用xpath方法解析
    select = lxml.html.document_fromstring(data)
    title = select.xpath(condition)  # 例子：'//div[@class="entry-tit"]/h1/text()'
    return title[0]


# 得到每一章的内容
def everyText(data, condition):
    select = lxml.html.document_fromstring(data)
    text = select.xpath(condition)  # 例子：'//div[@class="m-post"]/p/text()'
    endText = ''
    for i in range(len(text)):
        endText += text[i]
    return endText


# 拼接章节名和内容
def joinText(url, condition1, condition2):
    # 得到页面所有内容
    data = getData(url)

    # 得到页面小说标题
    title = everyTitle(data, condition1)
    # title = "".join(title.split('\xa0'))
    title = title.replace("\xa0", "")  # 去掉字符串中的空格

    # 得到页面小说内容
    text = everyText(data, condition2)
    # text = "".join(text.split('\xa0'))
    text = text.replace("\xa0", "")  # 去掉字符串中的空格

    # 拼接章节名和内容
    endContent = '\r\n' + title + text
    print(endContent)

    return endContent


# 得到书本
def getBook(num, url, condition1, condition2):
    '''
    endContent = joinText().encode('GBK')  # 编码为字节类型
    endContent = allText.decode('GBK')  # 解码为字符串
    '''
    endContent = joinText(url, condition1, condition2)
    number = num - 25414294
    with open('books\\%d.txt' % number, 'w') as f:
        print(number)
        f.write(endContent)


if __name__ == '__main__':
    condition1 = '//h1[@class="h1title"]/text()'
    condition2 = '//div[@id="htmlContent"]/text()'

    # 单进程执行
    # for i in [7548375, 7548391, 7548419]:
    #     url = 'https://www.69shu.org/book/17166/%d.html' % i
    #     getBook(num=i, url=url, condition1=condition1, condition2=condition2) 25415009

    # 多进程执行
    pool = Pool(30)
    for i in range(25414295, 25415009):
        url = 'https://www.69shu.org/book/82889/%d.html' % i
        print(url)
        pool.apply_async(getBook, (i, url, condition1, condition2,))  # 创建一个进程
    pool.close()  # 关闭进程池，表示不能再往进程池中添加进程，需要在join之前调用
    pool.join()  # 等待进程池中的所有子进程执行完毕，主进程才会结束。













