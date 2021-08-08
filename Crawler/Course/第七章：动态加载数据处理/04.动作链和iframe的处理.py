#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/7/2020 2:21 PM
# __software__ : PyCharm

from selenium import webdriver
# 导入动作链对应的类
from selenium.webdriver import ActionChains
import time


def main(browser):
    url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)

    # 如果定位的标签存在于iframe中，则必须通过如下操作才能进行标签定位
    browser.switch_to_frame('iframeResult')  # 作用域指定到iframe中
    div = browser.find_elements_by_id('draggable')[0]

    # 动作链
    action = webdriver.ActionChains(browser)

    for i in range(5):
        action.drag_and_drop_by_offset(div, 16, 0).perform()  # perform()立即执行动作链操作
        time.sleep(0.1)

    # 释放动作链
    action.release()


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path='./chromedriver')
    main(browser)


