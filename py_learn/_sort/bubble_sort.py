#!/usr/bin/python3
"""
冒泡排序
bubble + sort
"""

from py_learn.decoration import timing_func

data_count = 20


def bubble_sort(ds):
    for i in range(0, data_count):
        for j in range(0, data_count - i - 1):
            if ds[j] > ds[j + 1]:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]


random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]


@timing_func
def sort():
    bubble_sort(random_wait_sort)


print(f'time {sort()}')

print(random_wait_sort)
