#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 3/13/2021 9:15 PM
# __software__ : PyCharm

'''
将列表当做堆栈使用

列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来
'''


def stack_test():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(f'now stack: {stack}')

    leave_item = stack.pop()
    print(f'leave_item: {leave_item}, now stack: {stack}')

    leave_item = stack.pop()
    print(f'leave_item: {leave_item}, now stack: {stack}')


if __name__ == '__main__':
    stack_test()