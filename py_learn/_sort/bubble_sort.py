#!/usr/bin/python3
"""
冒泡排序
每一轮选一个最大的
bubble + sort
"""

from py_learn.decoration import timing_func


def bubble_sort(ds):
    for i in range(0, len(ds)):
        for j in range(0, len(ds) - i - 1):
            if ds[j] > ds[j + 1]:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]


random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]


@timing_func
def sort():
    bubble_sort(random_wait_sort)


print(f'time {sort()}')

print(random_wait_sort)
