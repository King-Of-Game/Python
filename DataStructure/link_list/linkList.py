#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 3/13/2021 9:44 PM
# __software__ : PyCharm

'''
单链表

'''


# 节点
class Node(object):
    def __init__(self, value=None):
        self.value = value  # 元素的值
        self.next = None  # 初始设置下一节点


# 单链表
class SingleLinkList(object):
    def __init__(self):
        self.head = Node()  # 创建头节点
        self.length = 0  # 初始化链表长度

    def __len__(self):
        return self.length

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    # 迭代所有节点
    def iter_node(self):
        cur_node = self.head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    # 链表头部添加元素
    def head_insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    # 删除头节点
    def head_del(self):
        if self.head is None:
            return False
        else:
            rm_node = self.head
            self.head = self.head.next
            self.length -= 1

    # 链表尾部添加元素
    def append(self, value):
        node = Node(value)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.length == 0:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self.length += 1

    # 指定索引添加元素
    def insert(self, index, value):
        # 如果索引在0或者以前，那么都当做头插法来做
        if index <= 0:
            self.head_insert(value)
        # 如果索引比原链表长，那么都当做尾插法来做
        elif index > self.length-1:
            self.append(value)
        else:
            per = self.head
            count = 0
            while count < index - 1:
                count += 1
                per = per.next
            # 当循环结束后，per指向索引前一个位置
            node = Node(value)
            node.next = per.next
            per.next = node
        self.length += 1

    # 删除节点
    def delete_node(self, value):
        if self.length == 0:
            return False
        else:
            cur_node = self.head
            pre_node = None

            for node in self.iter_node():
                if node.value == value:
                    # 先判断该节点是否是头节点
                    if node == self.head:
                        self.head = cur_node.next
                    else:
                        pre_node.next = cur_node.next
                    self.length -= 1
                    break

                pre_node = cur_node
                cur_node = cur_node.next

    # 修改节点
    def replace(self, old_value, new_value):
        pass


if __name__ == '__main__':
    singeLink = SingleLinkList()
    singeLink.append(2)
    # singeLink.append(3)
    singeLink.head_insert(1)
    # singeLink.insert(2, 4)

    print(f'当前单链表: {[i for i in singeLink]}')

    # singeLink.delete_node(3)
    # print(f'当前单链表: {[i for i in singeLink]}')

