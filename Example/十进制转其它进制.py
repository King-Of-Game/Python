#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/16/2021 4:06 PM
# __software__ : PyCharm


'''

用内置函数实现进制转换

'''


# 十进制转其它进制
def baseConversion():
    while True:
        input_txt = input('请输入一个正数（输入q退出）：')
        if input_txt in ['q', 'Q']:
            break
        try:
            number = int(input_txt)
            if number > 0:
                print(f'{number} 的二进制是: {bin(number)}')
                print(f'{number} 的八进制是: {oct(number)}')
                print(f'{number} 的十六进制是: {hex(number)}')
            else:
                raise ValueError

        except ValueError:
            print('请输入正数！')


# 其他进制转十进制
def baseConversion1():
    while True:
        input_txt = input('请输入2/8/16进制的数（输入q退出）：')
        if input_txt in ['q', 'Q']:
            break

        choice = int(input('请选择刚才输入数据对应的进制编号（1: 二进制, 2: 八进制, 3: 十六进制）:'))
        if choice == 1:
            baseNum = 2
        elif choice == 2:
            baseNum = 8
        else:
            baseNum = 16

        try:
            base10 = int(input_txt, baseNum)
            print(f'{input_txt} 是{baseNum}进制，它对应的十进制是{base10}')
        except ValueError:
            print('请确认您输入的数字和对应进制编号!')


if __name__ == '__main__':
    baseConversion()
    # baseConversion1()



