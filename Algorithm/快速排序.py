#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/23/2021 8:55 PM
# __software__ : PyCharm

'''

快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

步骤为：
1.挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
2.分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
3.递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

选取基准值不同对排序的时间性能有决定性影响。

'''
import random


# 快速排序：从小到大
'''
排序前: [3, 6, 8, 19, 1, 5]
left:[3, 6, 8, 1, 5] mid:[19] right:[]
left:[3, 6, 1, 5] mid:[8] right:[]
left:[] mid:[1] right:[3, 6, 5]
left:[3, 5] mid:[6] right:[]
left:[3] mid:[5] right:[]
[1, 3, 5, 6, 8, 19]
'''


# 快速排序：从小到大
def quickSort(lst, reverse=False):
    # 如果 == 1，那么 [] 执行以下代码，此时pivot[0]会报错
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst)//2]  # 基准值
    left = [i for i in lst if i < pivot]  # 分治给左边的序列排序
    middle = [i for i in lst if i == pivot]
    right = [i for i in lst if i > pivot]  # 分治给右边的序列排序
    if reverse:
        return quickSort(right, reverse) + middle + quickSort(left, reverse)
    return quickSort(left) + middle + quickSort(right)


if __name__ == '__main__':
    lst = [3, 6, 8, 19, 1, 5]
    # lst = random.sample(range(10), 10)
    print(f'排序前: {lst}')

    new_lst = quickSort(lst)
    print(f'从小到大快速排序后: {new_lst}')
    new_lst = quickSort(lst, reverse=True)
    print(f'从大到小快速排序后: {new_lst}')
