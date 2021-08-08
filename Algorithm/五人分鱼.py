#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/30/2021 4:20 PM
# __software__ : PyCharm

'''
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。
B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。
C、D、E依次醒来，也按同样的方法拿鱼。

问他们至少捕了多少条鱼?
'''


def min_fish(n):
    """
    n个人总共捕鱼数量为：S = Kn^n-(n-1) K为正整数
    最后一个人分得鱼的数量为：S(n) = K(n-1)^(n-1)-1 K为正整数
    因为求至少捕鱼数（所以：K为1）
    ----------
    n : 表示有多少个人
    """
    fish_numbers = n**n - n + 1
    print(f'至少捕了{fish_numbers}条鱼')


def min_fish1(n):
    total = 0
    while True:
        total += 1
        flag = True
        temp = total

        for i in range(n):
            if (temp - 1) % 5 == 0:
                temp = (temp - 1) / 5 * 4
            else:
                flag = False
                break

        if flag:
            print(f"{n} 个人至少捕了 {total} 条鱼。")
            break


if __name__ == '__main__':

    # min_fish(5)
    # min_fish1(5)

    least_fish = 0
    while True:
        flag = True

        now_fish = least_fish
        for i in range(5):
            if (now_fish - 1) % 5 == 0:
                now_fish = (now_fish-1) / 5 * 4
            else:
                flag = False
                break
        if flag:
            print(f"至少要有 {least_fish} 条鱼才能满足需求")
            break

        least_fish += 1



