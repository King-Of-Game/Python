#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/21/2021 3:53 PM
# __software__ : PyCharm


'''

给定一个字符串代码，然后使用 exec() 来执行字符串代码。

'''


def exec_code():
    LOC = '''
def jiecheng(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
    
num = 5
print(f'{num} 的阶乘是: {jiecheng(num)}')
    '''
    exec(LOC)


if __name__ == '__main__':
    exec_code()