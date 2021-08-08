#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 11/6/2020 11:00 PM
# __software__ : PyCharm

from selenium import webdriver
import time


def main(browser):
    url = 'https://so.gushiwen.cn/user/login.aspx'
    browser.get(url)

    # 给账号和密码赋值
    browser.find_elements_by_id('email')[0].send_keys('871437338@qq.com')
    browser.find_elements_by_id('pwd')[0].send_keys('zx454049162~')
    ranCode = input('请输入验证码')
    browser.find_elements_by_id('code')[0].send_keys(ranCode)

    # login
    browser.find_elements_by_id('denglu')[0].click()



if __name__ == '__main__':
    # browser = webdriver.Chrome(executable_path='D:\Google\Chrome\Application/chromedriver.exe')
    # main(browser)

    str = '129,87|45,72'
    str1 = '129,87'
    print(str.split('|'))
    print(str1.split('|'))
