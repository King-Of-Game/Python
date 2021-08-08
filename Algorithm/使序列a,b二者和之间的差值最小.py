#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 3/1/2021 3:47 PM
# __software__ : PyCharm

'''
有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。

1.分别计算a,b序列的和；
2.求a序列和与b序列和的差值的一半，记为half；
3.在和值大的序列中找出一个与和值小的序列中的元素max的差值最接近half的元素，记为min；
4.将max与min互换即可。
'''

# 方法有误
def abDifference(listA, listB):
    sumA = sum(listA)
    sumB = sum(listB)
    half = (sumA + sumB) / 2
    maxNum = max(listB) if sumA > sumB else max(listA)  #
    maxList = listA if sumA > sumB else listB
    minList = listB if sumA > sumB else listA

    print(f"大序列: {maxList}, 小序列: {minList}, 小序列的最大值: {maxNum}, half: {half}")

    difference = abs(half - abs(maxNum-maxList[0]))
    print(difference)
    minNum = 0
    for i in maxList:

        dif = abs(maxNum-i)
        print(f'|{i}-{maxNum}| = {dif}')






if __name__ == '__main__':
    listA = [1, 3, 5, 7, 9]
    listB = [2, 4, 6, 8, 10]

    abDifference(listA, listB)

