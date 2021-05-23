#!/usr/bin/python3
"""
选择排序
每一轮选一个最小的
selection + sort
"""


def selection_sort(ds):
    for i in range(0, len(ds) - 1):
        for j in range(i + 1, len(ds)):
            if ds[j] < ds[i]:
                ds[i], ds[j] = ds[j], ds[i]


random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

selection_sort(random_wait_sort)

print(random_wait_sort)
