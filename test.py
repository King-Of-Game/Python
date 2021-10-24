#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/9/29 23:54
# __software__ : PyCharm


def func(N):
    """
    数据结构选用：二维数组
    """
    # 初始化二位数组的元素
    lst = []
    for i in range(N):
        lst.append([0 for i in range(N)])
    # 记录每条线路走的步数
    steps = [N-1]  # 初始坐标不计步数
    if N > 1:
        for i in range(1, N):
            steps.append(N - i)
            steps.append(N - i)

    x, y = 0, 0  # 起始坐标
    lst[x][y] = 1
    xy_switch = 0    # 0: y坐标变化，1: x坐标变化
    directionX = 1   # 0: x坐标-1，1: x坐标+1
    directionY = 1   # 0: y坐标-1，1: y坐标+1

    # print(steps)
    num = 1
    for step in steps:
        for i in range(step):
            num += 1
            if xy_switch and directionX:
                x += 1
            if xy_switch and not directionX:
                x -= 1
            if not xy_switch and directionY:
                y += 1
            if not xy_switch and not directionY:
                y -= 1
            lst[x][y] = num
            print(f'x,y -> {x},{y} -> {num}')
            if i == step - 1:
                if xy_switch and directionX:
                    directionX = 0
                    break
                if xy_switch and not directionX:
                    directionX = 1
                    break
                if not xy_switch and directionY:
                    directionY = 0
                    break
                if not xy_switch and not directionY:
                    directionY = 1
                    break

        xy_switch = 0 if xy_switch else 1


    print(lst)
    for i in lst:
        print(i)


if __name__ == '__main__':
    func(4)

# 2 N N-1 N-1
# 3 N N-1 N-1 N-2 N-2
# 4 N N-1 N-1 N-2 N-2 N-1 N-1
