#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/3/22 17:15
# __software__ : PyCharm


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLink(object):
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
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def insert_head(self, value):
        """
        头部添加元素
        """
        try:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.length += 1
            return None
        except Exception as e:
            return e

    def append(self, value):
        """
        末尾添加元素
        """
        if self.length == 0:
            err = self.insert_head(value)
            if err is not None:
                return err
            return None
        try:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = Node(value)
            self.length += 1
            return None
        except Exception as e:
            return e

    def insert(self, value, index):
        """
        指定索引添加元素
        - value: 元素
        - index: 索引
        """
        if index == 0:
            err = self.insert_head(value)
            return err
        if index >= self.length:
            err = self.append(value)
            return err
        try:
            cur_node = self.head
            node = Node(value)
            while (index - 1) > 0:
                cur_node = cur_node.next
                index -= 1
            node.next = cur_node.next
            cur_node.next = node
            self.length += 1
            return None
        except Exception as e:
            return e

    def remove_head(self):
        """
        删除头部元素
        """
        if self.length == 0:
            self.head = None
            return None
        try:
            self.head = self.head.next
            self.length -= 1
            return None
        except Exception as e:
            return e

    def remove_end(self):
        """
        删除尾部元素
        """
        if self.length <= 1:
            err = self.remove_head()
            return err
        try:
            cur_node = self.head
            while cur_node.next.next is not None:
                cur_node = cur_node.next
            cur_node.next = None
            self.length -= 1

        except Exception as e:
            return e

    def remove(self, index):
        """
        根据索引删除元素
        """
        if index == 0:
            err = self.remove_head()
            return err
        try:
            cur_node = self.head
            while index-1 > 0:
                cur_node = cur_node.next
            cur_node.next = None
            self.length -= 1
            return None
        except Exception as e:
            return e


if __name__ == '__main__':
    singleLink = SingleLink()
    # 增
    singleLink.append(3)
    singleLink.insert_head(1)
    singleLink.append(4)
    singleLink.insert(value=2, index=1)

    # 删
    # singleLink.remove_head()
    # singleLink.remove_end()
    # singleLink.remove(1)
    for i in singleLink:
        pass
        # print(i, end=' ')

    for i in singleLink:
        print(i.value, end=' ')
