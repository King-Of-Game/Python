#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/3/22 17:15
# __software__ : PyCharm


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingeLinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        for node in self.iter_node():
            yield node

    def iter_node(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def insert_head(self, value):
        '''
        头插法
        '''
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, value):
        '''
        尾插法
        '''
        if self.length == 0:
            self.insert_head(value)
        else:
            cur_node = None
            for node in self.iter_node():
                cur_node = node
            node = Node(value)
            cur_node.next = node
            self.length += 1

    def insert_into(self, value, index):
        '''
        指定位置插入节点
        '''
        if index == 0:
            self.insert_head(value)
        elif index >= self.length:
            self.append(value)
        else:
            node = Node(value)
            for cur_node in self.iter_node():
                index -= 1
                if index <= 0:
                    node.next = cur_node.next
                    cur_node.next = node
                    self.length += 1
                    break

    def remove_head(self):
        '''
        头删
        '''
        if self.length == 0:
            pass
        else:
            self.head = self.head.next
            self.length -= 1

    def remove(self):
        '''
        尾删
        '''
        if self.length <= 1:
            self.remove_head()
        else:
            for cur_node in self.iter_node():
                if cur_node.next.next is None:
                    cur_node.next = None
                    self.length -= 1
                    break







if __name__ == '__main__':
    single = SingeLinkList()

    for i in single:
        print(i.value)

    # 增
    single.append(3)
    single.append(5)
    single.insert_head(1)
    single.insert_into(2, 1)
    single.insert_into(4, 3)

    # 删
    single.remove_head()
    single.remove()
    single.remove()
    single.remove()
    single.remove()
    for i in single:
        print(i.value, end=' ')

    print('')
    print(len(single))