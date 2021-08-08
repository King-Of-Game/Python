#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/17/2021 12:47 PM
# __software__ : PyCharm


'''
简单计算器
'''


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # 相加
    def add(self):
        return self.num1 + self.num2

    # 相减
    def subtract(self):
        return self.num1 - self.num2

    # 相乘
    def multiply(self):
        return self.num1 * self.num2

    # 相除
    def divide(self):
        return self.num1 / self.num2


if __name__ == '__main__':
    while True:
        input_txt = input('***简单计算器（输入q退出）***\n:')
        if input_txt in ['q', 'Q']:
            break

        try:
            num1 = int(input('请输入第一个数字: '))
            num2 = int(input('请输入第二个数字: '))
            choice = int(input(' 1)相加\n 2)相减\n 3)相乘\n 4)相除\n请输入你的选择: '))

            calculator = Calculator(num1, num2)
            if choice == 1:
                result = calculator.add()
                print(f'{num1} + {num2} = {result}')
            elif choice == 2:
                result = calculator.subtract()
                print(f'{num1} - {num2} = {result}')
            elif choice == 3:
                result = calculator.multiply()
                print(f'{num1} * {num2} = {result}')
            elif choice == 4:
                if num2 == 0:
                    print('分母不能为0！')
                    continue
                result = calculator.divide()
                print(f'{num1} / {num2} = {result}')
            else:
                print('请选择正确的序号')

        except ValueError:
            print('请输入正确的数字！')
