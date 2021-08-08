#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/8/2020 3:35 PM
# __software__ : PyCharm

from selenium import webdriver
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现selenium规避
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

import time


# 实现无可视化界面（无头浏览器）
def main(browser):
    url = 'https://www.baidu.com'
    browser.get(url)
    print(browser.page_source)
    # browser.quit()


if __name__ == '__main__':
    '''
     创建一个参数对象，用来控制chrome以无界面模式打开
    '''
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)

    '''
     如何实现让selenium规避被检测到的风险
    '''
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(executable_path='./chromedriver', options=option)

    main(browser)
