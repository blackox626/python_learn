def quick_sort(ds):
    def qsort(head, tail):
        if tail - head > 1:
            i = head
            j = tail
            pivot = ds[i]
            while i < j:
                if ds[i] > pivot or ds[j] < pivot:
                    ds[i], ds[j] = ds[j], ds[i]

                if ds[i] == pivot:
                    j -= 1
                else:
                    i += 1

            qsort(head, i - 1)
            qsort(i + 1, tail)

    def qsort2(head, tail):

        if head >= tail:
            return
        i = head
        j = tail

        pivot = ds[i]

        while i < j:
            while i < j and ds[j] > pivot:
                j = j - 1
            ds[i] = ds[j]

            while i < j and ds[i] <= pivot:
                i = i + 1
            ds[j] = ds[i]

        ds[j] = pivot

        qsort2(head, i - 1)
        qsort2(i + 1, tail)

    def qsort3(head, tail):
        if head >= tail:
            return
        i = head
        j = tail
        pivot = ds[i]

        while i < j:
            while i < j and ds[j] > pivot:
                j = j - 1

            while i < j and ds[i] <= pivot:
                i = i + 1

            ds[i], ds[j] = ds[j], ds[i]

        ds[head] = ds[j]
        ds[j] = pivot

        qsort3(head, i - 1)
        qsort3(i + 1, tail)

    qsort(0, len(ds) - 1)


def quick_sort2(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort2(array, low, left - 1)
    quick_sort2(array, left + 1, high)


random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

quick_sort(random_wait_sort)

quick_sort2(random_wait_sort, 0, 19)

print(random_wait_sort)
