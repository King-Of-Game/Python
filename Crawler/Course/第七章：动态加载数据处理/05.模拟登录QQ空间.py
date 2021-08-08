#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/7/2020 9:21 PM
# __software__ : PyCharm

from selenium import webdriver
import time


def main(browser):
    url = 'https://qzone.qq.com/'
    browser.get(url)

    # 切换iframe
    browser.switch_to_frame('login_frame')

    # 点击切换成账号密码登录
    browser.find_elements_by_id('switcher_plogin')[0].click()

    # 给账号和密码赋值
    browser.find_elements_by_id('u')[0].send_keys('871437338')
    browser.find_elements_by_id('p')[0].send_keys('wangyang97~')

    # login
    browser.find_elements_by_id('login_button')[0].click()



if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path='./chromedriver')

    main(browser)
