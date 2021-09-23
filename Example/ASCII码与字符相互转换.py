#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/16/2021 9:01 PM
# __software__ : PyCharm


def asciiAndChar():
    while True:
        if input('输入q/Q退出: ') in ['q', 'Q']:
            break

        # 用户输入字符
        char = input("请输入一个字符: ")

        # 用户输入ASCII码，并将输入的数字转为整型
        ASCII = int(input("请输入一个ASCII码: "))

        print(f"{char} 对应的ASCII 码为: {ord(char)}")
        print(f"{ASCII} 对应的字符为: {chr(ASCII)} ")


if __name__ == '__main__':
    # asciiAndChar()

    str1 = 'apple'
    str2 = 'APple'
    print(str1.capitalize())