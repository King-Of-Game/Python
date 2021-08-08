#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/6/2020 2:34 PM
# __software__ : PyCharm

from selenium import webdriver
from lxml import etree
from time import sleep

def main(url):
    # 实例化一个浏览器对象（传入浏览器的驱动程序）
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(url)
    # 获取浏览器当前页面的源码数据
    page_text = browser.page_source
    print(page_text)
    tree = etree.HTML(page_text)
    sleep(3)
    # browser.close()


if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    # 实例化一个浏览器对象（传入浏览器的驱动程序）
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(url)
    # 获取浏览器当前页面的源码数据
    page_text = browser.page_source
    # print(page_text)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="gzlist"]/li')
    for li in li_list:
        title = li.xpath('./dl/@title')[0]
        print(title)
    sleep(3)
    browser.quit()
    # browser.close()
