#!/usr/bin/python3
"""
选择排序
insert + sort
"""

data_count = 20


def selection_sort(ds):
    for i in range(0, data_count - 1):
        for j in range(i + 1, data_count):
            if ds[j] < ds[i]:
                ds[i], ds[j] = ds[j], ds[i]


random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

selection_sort(random_wait_sort)

print(random_wait_sort)
