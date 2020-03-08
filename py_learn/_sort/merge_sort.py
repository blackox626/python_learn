#!/usr/bin/python3
"""
归并排序
merge + sort
"""


def merge(lst, left, mid, right):
    lst_ = []

    p1 = left
    p2 = mid + 1

    while p1 <= mid and p2 <= right:
        if lst[p1] < lst[p2]:
            lst_.append(lst[p1])
            p1 += 1
        else:
            lst_.append(lst[p2])
            p2 += 1

    if p1 <= mid:
        lst_.extend(lst[p1:mid + 1])
    if p2 <= right:
        lst_.extend(lst[p2:right + 1])

    for i, l in enumerate(lst_):
        lst[left + i] = l


def sort(lst, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2
    sort(lst, left, mid)
    sort(lst, mid + 1, right)
    merge(lst, left, mid, right)


def merge_sort(ds):
    left = 0
    right = len(ds)
    sort(ds, left, right - 1)


# print(merge([1, 3, 5, 2, 4], 0, 2, 4))

random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

merge_sort(random_wait_sort)

print(random_wait_sort)
