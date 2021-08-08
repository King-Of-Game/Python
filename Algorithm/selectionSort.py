# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/7/13

'''
选择排序：从小到大排序
第一轮从第1个元素开始（第二轮第2个....），依次跟后面所有的元素比较，把小的放前面（从前往后整理）
'''


def selectSort(lst):
    length = len(lst)
    for i in range(length - 1):  # 总共比较（length - 1）轮

        min_index = i
        for j in range(i+1, length):  # 第i个元素依次和后面的比较
            if lst[min_index] > lst[j]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]
    print(f"从小到大排序后: {lst}")

    # 从大到小
    for i in range(length - 1):

        max_index = i
        for j in range(i+1, length):
            if lst[max_index] < lst[j]:
                max_index = j
        lst[i], lst[max_index] = lst[max_index], lst[i]

    print(f"从大到小排序后: {lst}")


if __name__ == '__main__':
    lst = [4, 5, 3, 6, 1, 2]
    print(f"选择排序前: {lst}")

    selectSort(lst)


