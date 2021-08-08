#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/5/1010 6:13 PM
# __software__ : PyCharm

from selenium import webdriver
from time import sleep


def main(url):
    # 浏览器的驱动位置
    driver = webdriver.Chrome(r'chromedriver.exe')
    driver.get(url)

    # 查找页面的‘设置’选项，并进行点击
    driver.find_elements_by_id('s-usersetting-top')[0].click()
    sleep(1)
    # 打开设置后找到“搜索设置”选项，设置为每页显示50条
    driver.find_elements_by_link_text('搜索设置')[0].click()
    sleep(1)
    # 利用xpath选中每页显示50条
    driver.find_element_by_xpath('//*[@id="nr_3"]').click()
    sleep(1)
    # 点击保存设置
    driver.find_elements_by_xpath('//*[@id="se-setting-7"]//a[2]')[0].click()
    sleep(1)
    # 处理弹出的警告页面   确定accept() 和 取消dismiss()
    driver.switch_to_alert().accept()
    sleep(1)

    # 找到百度的输入框，并输入 美女
    driver.find_element_by_id('kw').send_keys('美女')
    sleep(1)
    # 点击搜索按钮
    driver.find_element_by_id('su').click()
    sleep(1)
    # 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
    driver.find_elements_by_link_text('图片')[0].click()
    sleep(10)
    # 关闭浏览器
    driver.quit()



if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    main(url)
