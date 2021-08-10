#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 3/13/2021 9:05 PM
# __software__ : PyCharm

'''
将列表当作队列使用

可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来
把列表当做队列用效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个个地向后、移动）。
'''

from collections import deque


def queue_test():
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Marry")
    queue.append("Jack")
    print(f"now queue: {queue}, type: {type(queue)}")
    # 先进先出
    leave_item = queue.popleft()
    print(f"{leave_item} left, now queue: {queue}")

    leave_item = queue.popleft()
    print(f"{leave_item} left, now queue: {queue}")


if __name__ == '__main__':
    queue_test()
