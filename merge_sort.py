import time

def merge_sort(data, update_visualization, speed):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = arr[l:m+1]
        R = arr[m+1:r+1]
        i = j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            update_visualization(arr)
            time.sleep(1 / speed())
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            merge_sort_helper(arr, l, m)
            merge_sort_helper(arr, m+1, r)
            merge(arr, l, m, r)

    merge_sort_helper(data, 0, len(data)-1)
