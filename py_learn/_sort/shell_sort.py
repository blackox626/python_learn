def shell_sort(arr):
    n = len(arr)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)


random_wait_sort = [12, 34, 32, 24, 28, 39, 5, 22, 11, 25,
                    33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

shell_sort(random_wait_sort)

print(random_wait_sort)
