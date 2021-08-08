#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/3/22 17:15
# __software__ : PyCharm


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkList(object):

    def __init__(self):
        self.head = Node()
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        cur_node = self.head

        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def insert_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, value):
        node = Node(value)

        if self.length == 0:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node

        self.length += 1


            # cur_node = node


if __name__ == '__main__':
    sLinkList = SingleLinkList()

    sLinkList.insert_head(2)
    sLinkList.insert_head('jack')
    print(f'当前链表元素: {[i for i in sLinkList]}')

    sLinkList.append('lucy')
    print(f'当前链表元素: {[i for i in sLinkList]}')
