"""
different sort
"""


class DifferentSort:
    def __init__(self, lst):
        self.lst = lst
        self.length = len(lst)

    def __len__(self):
        return self.length

    # 冒泡排序
    def bubble_sort(self):
        for i in range(self.length - 1):
            for j in range(len(self.lst) - 1 - i):
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
        print(f'从小到大冒泡排序：{self.lst}')
        for i in range(self.length - 1):
            for j in range(len(self.lst) - 1 - i):
                if self.lst[j] < self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
        print(f'从大到小冒泡排序：{self.lst}')

    # 选择排序
    def select_sort(self):
        for i in range(self.length - 1):
            for j in range(i + 1, self.length):
                if self.lst[i] > self.lst[j]:
                    self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
        print(f'从小到大选择排序：{self.lst}')
        for i in range(self.length - 1):
            for j in range(i + 1, self.length):
                if self.lst[i] < self.lst[j]:
                    self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
        print(f'从小到大选择排序：{self.lst}')

    # 插入排序
    def insert_sort(self):
        for i in range(1, self.length):
            key = self.lst[i]
            j = i
            while j > 0 and key < self.lst[j - 1]:
                self.lst[j] = self.lst[j - 1]

                j -= 1
            self.lst[j] = key
        print(f'从小到大插入排序：{self.lst}')
        for i in range(1, self.length):
            key = self.lst[i]
            j = i
            while j > 0 and key > self.lst[j - 1]:
                self.lst[j] = self.lst[j - 1]
                j -= 1
            self.lst[j] = key
        print(f'从大到小插入排序：{self.lst}')

    # 希尔排序
    def hil_sort(self):
        mid = self.length // 2
        while mid > 0:
            for i in range(mid, self.length):
                temp = self.lst[i]
                j = i
                while j >= mid and temp < self.lst[j - mid]:
                    self.lst[j] = self.lst[j - mid]
                    j -= mid
                self.lst[j] = temp

            mid = mid // 2
        print(f'从小到大希尔排序：{self.lst}')

        mid = self.length // 2
        while mid > 0:
            for i in range(mid, self.length):
                temp = self.lst[i]
                j = i
                while j >= mid and temp > self.lst[j - mid]:
                    self.lst[j] = self.lst[j - mid]
                    j -= mid
                self.lst[j] = temp
            mid = mid // 2
        print(f'从大到小希尔排序：{self.lst}')

    # 快速排序
    def quick_sort(self, lst, reverse=0):
        if len(lst) <= 1:
            return lst
        pivot = lst[len(lst) // 2]

        small = [i for i in lst if i < pivot]
        mid = [i for i in lst if i == pivot]
        big = [i for i in lst if i > pivot]
        if not reverse:
            return self.quick_sort(small, reverse=reverse) + mid + self.quick_sort(big, reverse=reverse)
        else:
            return self.quick_sort(big, reverse=reverse) + mid + self.quick_sort(small, reverse=reverse)

    # 二分查找
    def binary_search(self, lst, left, right, target):
        """
        二分查找必须基于有序数列
        lst: 被搜索的数列
        left: 左边界
        target: 目标值
        right: 右边界
        """
        mid_index = (left + right) // 2
        if right > left:
            if lst[mid_index] == target:
                print(f'目标元素位于第{mid_index + 1}个')
            elif lst[mid_index] < target:
                return self.binary_search(lst, lst, mid_index, target)
            else:
                return self.binary_search(lst, mid_index + 1, right, target)
        else:
            print(f'找不到目标元素')






def kuaisu(lst):
    if len(lst) <= 1:
        return lst
    mid_index = len(lst) // 2
    pivot = lst[mid_index]

    left = [i for i in lst if i < pivot]
    mid = [i for i in lst if i == pivot]
    right = [i for i in lst if i > pivot]
    return kuaisu(left) + mid + kuaisu(right)






if __name__ == '__main__':
    non_sort_list = [3, 6, 8, 1, 5]
    print(f'排序前：{non_sort_list}')

    result = kuaisu(non_sort_list)
    print(result)






# difSort = DifferentSort(lst=non_sort_list)

# difSort.bubble_sort()
# difSort.select_sort()
# difSort.insert_sort()
# difSort.hil_sort()
# result = difSort.quick_sort(difSort.lst)
# print(f'从小到大快速排序：{result}')
# result = difSort.quick_sort(difSort.lst, reverse=1)
# print(f'从大到小快速排序：{result}')

# difSort.binary_search(difSort.lst, 0, difSort.length, 5)
