#!/usr/bin/python3
"""
堆排序
heap + sort
"""

data_count = 20


def heap_sort(ds):
    def heap_adjust(head, tail):
        i = head * 2 + 1  # head的左孩子
        while i < tail:
            if i + 1 < tail and ds[i] < ds[i + 1]:  # 选择一个更大的孩子
                i += 1
            if ds[i] <= ds[head]:
                break
            ds[head], ds[i] = ds[i], ds[head]
            head = i
            i = i * 2 + 1

    # 建立一个最大堆，从最后一个父节点开始调整
    for i in range(data_count // 2 - 1, -1, -1):
        heap_adjust(i, data_count)
    for i in range(data_count - 1, 0, -1):
        ds[i], ds[0] = ds[0], ds[i]  # 把最大值放在位置i处
        heap_adjust(0, i)  # 从0~i-1进行堆调整


random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

heap_sort(random_wait_sort)

print(random_wait_sort)
