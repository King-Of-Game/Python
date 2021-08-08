#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/19/2021 11:14 AM
# __software__ : PyCharm


'''

通过内置函数判断字符串

'''


def strTest1():
    print("测试实例一")
    string = "runoob.com"
    print(string.isalnum())  # 判断所有字符都是数字或者字母
    print(string.isalpha())  # 判断所有字符都是字母
    print(string.isdigit())  # 判断所有字符都是数字
    print(string.islower())  # 判断所有字符都是小写
    print(string.isupper())  # 判断所有字符都是大写
    print(string.istitle())  # 判断所有单词都是首字母大写，像标题
    print(string.isspace())  # 判断所有字符都是空白字符、\t、\n、\r


def strTest2():
    print("测试实例二")
    string = "runoob"
    print(string.isalnum())
    print(string.isalpha())
    print(string.isdigit())
    print(string.islower())
    print(string.isupper())
    print(string.istitle())
    print(string.isspace())


if __name__ == '__main__':
    strTest1()
