# merge_sort.py

import time

def merge_sort(data, draw_data, speed):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * (n1)
        R = [0] * (n2)
        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

        color_array = ["red" if x >= l and x <= r else "blue" for x in range(len(data))]
        draw_data(data, color_array)
        time.sleep(speed)

    def merge_sort_helper(arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            merge_sort_helper(arr, l, m)
            merge_sort_helper(arr, m + 1, r)
            merge(arr, l, m, r)

    merge_sort_helper(data, 0, len(data) - 1)
