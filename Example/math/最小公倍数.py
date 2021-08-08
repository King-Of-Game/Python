#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/16/2021 9:42 PM
# __software__ : PyCharm

'''

输入两个数字，计算他们之间的最小公倍数

其它方法：
1、最小公倍数等于两个数的乘积除以最大公约数
2、当最大值为最小公倍数时，返回最大值；当最大值不为最小公倍数时，最小公倍数为最大值的倍数。

'''


# 普通方法
def lcm1(num1, num2):
    bigger = max(num1,num2)
    count = 0
    while True:
        count += 1
        if bigger % num1 == 0 and bigger % num2 == 0:
            print(f'{num1} 和 {num2} 之间的最小公倍数数是: {bigger}')
            print(f'循环了{count} 次得到了结果')
            break
        bigger += 1


# 通过"其他方法2"优化普通方法
def lcm2(num1, num2):
    bigger = max(num1,num2)
    smaller = min(num1,num2)
    count = 0

    while True:
        count += 1
        if bigger % smaller == 0:
            print(f'{num1} 和 {num2} 之间的最小公倍数数是: {bigger}')
            print(f'循环了{count} 次得到了结果')
            break
        else:
            result = bigger * (count + 1)
            if result % smaller == 0:
                print(f'{num1} 和 {num2} 之间的最小公倍数数是: {result}')
                print(f'循环了{count} 次得到了结果')
                break


# 最小公倍数等于两个数的乘积除以最大公约数
# 辗转相除法计算最大公约数
def f1(a, b):
    count = 1
    while b != 0:
        count += 1
        a, b = b, a % b
    print(f'循环了{count} 次得到了结果')
    return a


def lcm3(num1, num2):
    hcf = f1(num1, num2)

    result = (num1 * num2) // hcf
    print(f'{num1} 和 {num2} 之间的最小公倍数数是: {result}')




if __name__ == '__main__':
    num1 = int(input('请输入第一个数字: '))
    num2 = int(input('请输入第二个数字: '))
    # lcm1(num1, num2)
    lcm2(num1, num2)
    # lcm3(num1, num2)
