#!/usr/bin/python3
"""
插入排序
insert + sort
"""


def insert_sort(ds):
    for i in range(1, len(ds)):
        key = ds[i]
        j = i - 1
        while j >= 0 and key < ds[j]:
            ds[j + 1] = ds[j]
            j -= 1
        ds[j + 1] = key


random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

insert_sort(random_wait_sort)

print(random_wait_sort)
