# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/7/13

'''
冒泡排序：从小到大排序
每轮都从第一个元素开始，相邻的两个元素比较，把大的放后面（从后往前整理）
'''


def bubbleSort(lst):
    length = len(lst)
    # 从小到大
    for i in range(length - 1):  # 一共比较(length - 1)轮
        for j in range(length - 1 - i):  # 每轮比较的次数
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j+1], lst[j]
    print(f"从小到大排序后: {lst}")

    # 从大到小
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j + 1] = lst[j+1], lst[j]
    print(f"从大到小排序后: {lst}")


if __name__ == '__main__':
    lst = [4, 5, 3, 6, 1, 2]
    print(f"冒泡排序前: {lst}")
    
    bubbleSort(lst)


