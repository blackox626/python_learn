def partition(lst, left, right):
    pivot = lst[left]
    i, j = left, right
    while i < j:
        while i < j and lst[j] >= pivot:
            j = j - 1
        lst[i] = lst[j]
        while i < j and lst[i] < pivot:
            i = i + 1
        lst[j] = lst[i]
    lst[j] = pivot
    return j


# 快速排序
def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index - 1)
        quicksort(nums, index + 1, right)


arr = [1, 3, 2, 2, 0]
quicksort(arr, 0, len(arr) - 1)
print(arr)


def topk_split(nums, k, left, right):
    index = partition(nums, left, right)
    if index == k:
        return
    elif index > k:
        return topk_split(nums, k, left, index - 1)
    else:
        return topk_split(nums, k, index + 1, right)


arr = [1, 3, -2, 3, 0, -19]
topk = 2
print(topk_split(arr, topk, 0, len(arr) - 1))
print(arr)
