#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/19/2021 6:07 PM
# __software__ : PyCharm

'''

约瑟夫生者死者小游戏

30 个人在一条船上，超载，需要 15 人下船。
于是人们排成一队，排队的位置即为他们的编号。
报数，从 1 开始，数到 9 的人下船。
如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？

'''


def ysfGame1():
    people_list = list(range(1, 31))
    step = 0  # 记录步数
    leave_list = []  # 所有离开人的名单

    while len(people_list) > 15:

        temp_list = []  # 临时存放每一次循环离开的人
        for i in people_list:
            step += 1
            if step % 9 == 0:
                temp_list.append(i)

        for temp in temp_list:
            people_list.remove(temp)
            leave_list.append(temp)

    print(f'留在船上的人: \n{people_list}')
    print(f'下船的人: \n{leave_list}')


def ysfGame2():
    people = list(range(1, 31))
    while len(people) > 15:
        i = 1
        while i < 9:
            people.append(people.pop(0))  # 不是第九个就在队尾重新排队
            i += 1
        print('{:2d}号下船了'.format(people.pop(0)))


def ysfGame3():
    people = list(range(1, 31))
    count = 0  # 统计报数次数
    while len(people) > 15:
        count += 1
        if count % 9 == 0:
            print(f'{people.pop(0)} 号下船了')

        else:
            people.append(people.pop(0))

    print(f'报数: {count} 次')
    print(f'船上剩余人员: {people}')


if __name__ == '__main__':
    # ysfGame2()
    # ysfGame1()
    # ysfGame3()


    people = [i for i in range(1,31)]
    count = 0

    while len(people) > 15:
        count += 1

        if count % 9 == 0:
            leave = people.pop(0)
            print(f'{leave} 号下船了')
        else:
            people.append(people.pop(0))
    print(f'一共报数: {count} 次，船上剩下{people}')













