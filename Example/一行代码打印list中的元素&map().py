#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/21/2021 7:19 PM
# __software__ : PyCharm


# 输出strlist
strlist=['a','b','c','d']

print(''.join(strlist))  # 不换行输出abcd
for i in strlist: print(i, end='')  # 不换行输出abcd
print()
for i in strlist: print(i)  # 换行输出abcd

# 输出intlist
intlist=[1,2,3,4]

print(''.join(map(str, intlist)))  # 不换行输出
for i in intlist: print(i, end='')  # 不换行输出
print()
for i in intlist: print(i)  # 换行输出
print(''.join(sorted(str(i) for i in intlist)))  # 不换行输出

#print()作用相当于换行，只是为了你方便查看返回代码。和输出列表代码不相关。