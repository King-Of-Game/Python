#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/6/2020 10:20 PM
# __software__ : PyCharm

from selenium import webdriver
from time import sleep





if __name__ == '__main__':
    url = 'https://www.taobao.com/'
    # 浏览器的驱动位置
    browse = webdriver.Chrome(r'./chromedriver.exe')
    browse.get(url)

    # 标签定位
    search_input = browse.find_element_by_id('q')
    # 标签交互
    search_input.send_keys('gtx2080')

    # 执行js
    browse.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(2)

    # 点击搜索按钮
    btn = browse.find_element_by_css_selector('button.btn-search')
    btn.click()

    browse.get('https://www.baidu.com')
    sleep(2)
    # 后退
    browse.back()
    sleep(2)
    # 前进
    browse.forward()

    # 隐式等待
    # browse.implicitly_wait(3000)
    # 关闭浏览器
    # browse.close()

