def quick_sort(ds):
    def qsort(head, tail):
        if tail - head > 1:
            i = head
            j = tail - 1
            pivot = ds[j]
            while i < j:
                if ds[i] > pivot or ds[j] < pivot:
                    ds[i], ds[j] = ds[j], ds[i]
                if ds[i] == pivot:
                    j -= 1
                else:
                    i += 1
            qsort(head, i)
            qsort(i + 1, tail)

    qsort(0, len(ds))


random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

quick_sort(random_wait_sort)

print(random_wait_sort)
