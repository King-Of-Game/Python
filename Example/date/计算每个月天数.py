#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/19/2021 11:31 AM
# __software__ : PyCharm


'''

通过 calendar 模块来计算每个月的天数

'''

import calendar


# 获取某年某月的天数，那个月第一天是星期几
def week_month():
    while True:
        input_text = input('输入q退出: ')
        if input_text in ['q', 'Q']:
            break

        try:
            year = int(input('请输入年份: '))
            month = int(input('请输入月份: '))

            # 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
            monthRange = calendar.monthrange(year, month)
            print(f'{year}/{month} 有 {monthRange[1]} 天, 这个月的第一天是星期 {monthRange[0]+1}')
        except ValueError:
            print('请输入正确的年份和月份！')


if __name__ == '__main__':
    week_month()