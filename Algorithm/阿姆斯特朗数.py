#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/16/2021 2:45 PM
# __software__ : PyCharm


'''

阿姆斯特朗数：
一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
例如1^3 + 5^3 + 3^3 = 153。

1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

'''


# 手动输入一个数判断是否为阿姆利斯朗数
def amu_number1():
    while True:
        try:
            number = int(input('请输入一个数字: '))
            numStr = str(number)
            result = 0
            for i in numStr:
                result += int(i) ** len(numStr)
            if result == number:
                print(f'{number} 是阿姆斯特朗数')
                break
            else:
                print(f'{number} 不是阿姆斯特朗数')
                continue
        except ValueError:
            print('请输入大于零的整数！')


# 获取指定区间内的阿姆斯特朗数
def amu_number2(x, y):
    print(f'{x}~{y}以内的阿姆斯特朗数：')
    for i in range(x, y+1):

        numStr = str(i)
        n = len(numStr)  # 指数

        # 计算当前数字
        result = 0
        for j in numStr:
            result += int(j) ** n

        if result == i:
            print(f'{i} ', end=' ')


# 获取指定区间内的阿姆斯特朗数
def amu_number3():
    # 获取用户输入数字
    lower = int(input("最小值: "))
    upper = int(input("最大值: "))

    for num in range(lower, upper + 1):
        # 初始化 sum
        result = 0
        # 指数
        n = len(str(num))

        # 检测
        temp = num
        while temp > 0:
            digit = temp % 10
            result += digit ** n
            temp = temp // 10

        if num == result:
            print(result)


if __name__ == '__main__':
    # amu_number1()
    # amu_number2(1, 1000)
    # amu_number3()

    for i in range(1, 1000):
        result = 0

        index = len(str(i))  # 指数
        temp = i
        while temp > 0:
            digit = temp % 10
            result += digit ** index  # 个位
            temp = temp // 10

        if result == i:
            print(i)

